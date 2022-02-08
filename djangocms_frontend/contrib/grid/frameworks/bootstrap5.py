from djangocms_frontend import settings


def get_row_cols_grid_values(instance):
    classes = []
    for device in settings.DEVICE_SIZES:
        size = getattr(instance, f"row_cols_{device}", None)
        if isinstance(size, int):
            if device == "xs":
                classes.append(f"row-cols-{int(size)}")
            else:
                classes.append(f"row-cols-{device}-{int(size)}")
    return classes


class GridContainerRenderMixin:
    def render(self, context, instance, placeholder):
        instance.add_classes(instance.container_type)
        return super().render(context, instance, placeholder)


class GridRowRenderMixin:
    render_template = "djangocms_frontend/bootstrap5/grid_row.html"

    def render(self, context, instance, placeholder):
        instance.add_classes(
            "row",
            instance.vertical_alignment,
            instance.horizontal_alignment,
        )
        if instance.gutters or (
            instance.parent and instance.parent.plugin_type == "CardPlugin"
        ):  # no gutters if inside card
            instance.add_classes("g-0")
        instance.add_classes(get_row_cols_grid_values(instance))
        return super().render(context, instance, placeholder)


class GridColumnRenderMixin:
    def render(self, context, instance, placeholder):
        instance.add_classes(
            f"col text-{instance.text_alignment}"
            if instance.config.get("text_alignment", None)
            else "col"
        )
        return super().render(context, instance, placeholder)
