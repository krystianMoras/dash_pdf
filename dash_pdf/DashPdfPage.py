# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashPdfPage(Component):
    """A DashPdfPage component.


Keyword arguments:

- pageNumber (number; optional):
    Page number to be displayed.

- width (number; optional):
    Width of the page."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_pdf'
    _type = 'DashPdfPage'
    @_explicitize_args
    def __init__(self, pageNumber=Component.UNDEFINED, width=Component.UNDEFINED, **kwargs):
        self._prop_names = ['pageNumber', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['pageNumber', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashPdfPage, self).__init__(**args)
