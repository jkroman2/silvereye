from django.contrib import admin, auth

from silvereye.models import Publisher, PublisherMetrics, FileSubmission, PublisherMonthlyCounts

from import_export.admin import ImportExportModelAdmin

class UserAdmin(ImportExportModelAdmin):
    pass

class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'publisher_id',
        'publisher_name',
        'publisher_scheme',
        'uri',
        'ocid_prefix',
        'contact_name',
        'contact_email',
        'contact_telephone',
    )
    list_editable = (
        'publisher_name',
        'contact_name',
        'contact_email',
        'contact_telephone',
    )


admin.site.register(Publisher, PublisherAdmin)


class PublisherMetricsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PublisherMetrics._meta.get_fields()]
    readonly_fields = [field.name for field in PublisherMetrics._meta.get_fields()]


admin.site.register(PublisherMetrics, PublisherMetricsAdmin)


class PublisherMonthlyCountsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PublisherMonthlyCounts._meta.get_fields()]
    readonly_fields = [field.name for field in PublisherMonthlyCounts._meta.get_fields()]


admin.site.register(PublisherMonthlyCounts, PublisherMonthlyCountsAdmin)


class FileSubmissionAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'source_url',
                    'original_file',
                    'current_app',
                    'created',
                    'modified',
                    'rendered',
                    'schema_version',
                    'data_schema_version',
                    'form_name',
                    # 'supplied_data',
                    'publisher']


admin.site.register(FileSubmission, FileSubmissionAdmin)
