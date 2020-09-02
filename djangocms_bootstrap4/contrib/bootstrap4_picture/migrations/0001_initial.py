# Generated by Django 1.9.13 on 2017-10-13 19:22
import django.db.models.deletion
from django.db import migrations, models

import cms.models.fields

import djangocms_attributes_field.fields
import filer.fields.image
from djangocms_picture.models import (
    LINK_TARGET, PICTURE_ALIGNMENT, get_templates,
)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4Picture',
            fields=[
                ('template', models.CharField(choices=get_templates(), default=get_templates()[0][0], max_length=255, verbose_name='Template')),
                ('external_picture', models.URLField(blank=True, help_text='If provided, overrides the embedded image. Certain options such as cropping are not applicable to external images.', max_length=255, verbose_name='External image')),
                ('width', models.PositiveIntegerField(blank=True, help_text='The image width as number in pixels. Example: "720" and not "720px".', null=True, verbose_name='Width')),
                ('height', models.PositiveIntegerField(blank=True, help_text='The image height as number in pixels. Example: "720" and not "720px".', null=True, verbose_name='Height')),
                ('alignment', models.CharField(blank=True, choices=PICTURE_ALIGNMENT, help_text='Aligns the image according to the selected option.', max_length=255, verbose_name='Alignment')),
                ('caption_text', models.TextField(blank=True, help_text='Provide a description, attribution, copyright or other information.', verbose_name='Caption text')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('link_url', models.URLField(blank=True, help_text='Wraps the image in a link to an external URL.', max_length=2040, verbose_name='External URL')),
                ('link_target', models.CharField(blank=True, choices=LINK_TARGET, max_length=255, verbose_name='Link target')),
                ('link_attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Link attributes')),
                ('use_automatic_scaling', models.BooleanField(default=True, help_text='Uses the placeholder dimensions to automatically calculate the size.', verbose_name='Automatic scaling')),
                ('use_no_cropping', models.BooleanField(default=False, help_text='Outputs the raw image without cropping.', verbose_name='Use original image')),
                ('use_crop', models.BooleanField(default=False, help_text='Crops the image according to the thumbnail settings provided in the template.', verbose_name='Crop image')),
                ('use_upscale', models.BooleanField(default=False, help_text='Upscales the image to the size of the thumbnail settings in the template.', verbose_name='Upscale image')),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bootstrap4_picture_bootstrap4picture', serialize=False, to='cms.CMSPlugin')),
                ('picture_fluid', models.BooleanField(default=True, help_text='Adds the .img-fluid class to make the image responsive.', verbose_name='Responsive')),
                ('picture_rounded', models.BooleanField(default=False, help_text='Adds the .rounded class for round corners.', verbose_name='Rounded')),
                ('picture_thumbnail', models.BooleanField(default=False, help_text='Adds the .img-thumbnail class.', verbose_name='Thumbnail')),
                ('link_page', cms.models.fields.PageField(blank=True, help_text='Wraps the image in a link to an internal (page) URL.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page', verbose_name='Internal URL')),
                ('picture', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.Image', verbose_name='Image')),
                ('thumbnail_options', models.ForeignKey(blank=True, help_text='Overrides width, height, and crop; scales up to the provided preset dimensions.', null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.ThumbnailOption', verbose_name='Thumbnail options')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
