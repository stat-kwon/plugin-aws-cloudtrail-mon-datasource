from schematics import Model
from schematics.types import ListType, ModelType, PolyModelType
from spaceone.monitoring.model.metadata.metadata_dynamic_layout import BaseLayoutField, QuerySearchTableDynamicLayout
from spaceone.monitoring.model.metadata.metadata_dynamic_search import BaseDynamicSearch
from spaceone.monitoring.model.metadata.metadata_dynamic_widget import BaseDynamicWidget


class MetaDataViewTable(Model):
    layout = PolyModelType(BaseLayoutField)


class MetaDataViewSubData(Model):
    layouts = ListType(PolyModelType(BaseLayoutField))


class MetaDataView(Model):
    table = PolyModelType(MetaDataViewTable, serialize_when_none=False)
    sub_data = PolyModelType(MetaDataViewSubData, serialize_when_none=False)
    search = ListType(PolyModelType(BaseDynamicSearch), serialize_when_none=False)
    widget = ListType(PolyModelType(BaseDynamicWidget), serialize_when_none=False)


class LogMetadata(Model):
    view = ModelType(MetaDataView)

    @classmethod
    def set_fields(cls, name='', fields=[]):
        _table = MetaDataViewTable({'layout': QuerySearchTableDynamicLayout.set_fields(name, fields)})
        return cls({'view': MetaDataView({'table': _table})})

    @classmethod
    def set_meta(cls, name='', fields=[], search=[], widget=[]):
        table_meta = MetaDataViewTable({'layout': QuerySearchTableDynamicLayout.set_fields(name, fields)})
        return cls({'view': MetaDataView({'table': table_meta, 'search': search, 'widget': widget})})