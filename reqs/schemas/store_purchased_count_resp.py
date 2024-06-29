from reprlib import repr as limitedRepr


from typing import List



class StorePurchasedCountResp:
    class _data:
            class _attributes:
                    class _dates:



                            _types_map = {
                                'years': {'type': list, 'subtype': dict},
                            }
                            _formats_map = {
                            }
                            _validations_map = {
                                'years': { 'required': True,},
                            }

                            def __init__(self
                                    , years: List[dict]
                        =None            ):
                                pass
                                self.__years = years
                            
                            def _get_years(self):
                                return self.__years
                            def _set_years(self, value):
                                if  not isinstance(value, list):
                                    raise TypeError("years must be list")
                                if  not all(isinstance(i, dict) for i in value):
                                    raise TypeError("years list values must be dict")

                                self.__years = value
                            years = property(_get_years, _set_years)
                            

                            @staticmethod
                            def from_dict(d):
                                v = {}
                                if "years" in d:
                                    v["years"] = [dict.from_dict(p) if hasattr(dict, 'from_dict') else p for p in d["years"]]
                                return StorePurchasedCountResp._data._attributes._dates(**v)


                            def as_dict(self):
                                d = {}
                                if self.__years is not None:
                                    d['years'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__years]
                                return d

                            def __repr__(self):
                                return "<Class _dates. years: {}>".format(limitedRepr(self.__years[:20] if isinstance(self.__years, bytes) else self.__years))




                    _types_map = {
                        'dates': {'type': _dates, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'dates': { 'required': True,},
                    }

                    def __init__(self
                            , dates: _dates=None            ):
                        pass
                        self.__dates = dates
                    
                    def _get_dates(self):
                        return self.__dates
                    def _set_dates(self, value):
                        if  not isinstance(value, StorePurchasedCountResp._data._attributes._dates):
                            raise TypeError("dates must be StorePurchasedCountResp._data._attributes._dates")

                        self.__dates = value
                    dates = property(_get_dates, _set_dates)
                    

                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "dates" in d:
                            v["dates"] = StorePurchasedCountResp._data._attributes._dates.from_dict(d["dates"]) if hasattr(StorePurchasedCountResp._data._attributes._dates, 'from_dict') else d["dates"]
                        return StorePurchasedCountResp._data._attributes(**v)


                    def as_dict(self):
                        d = {}
                        if self.__dates is not None:
                            d['dates'] = self.__dates.as_dict() if hasattr(self.__dates, 'as_dict') else self.__dates
                        return d

                    def __repr__(self):
                        return "<Class _attributes. dates: {}>".format(limitedRepr(self.__dates[:20] if isinstance(self.__dates, bytes) else self.__dates))




            _types_map = {
                'attributes': {'type': _attributes, 'subtype': None},
                'id': {'type': str, 'subtype': None},
                'type': {'type': str, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'attributes': { 'required': True,},
                'id': { 'required': True,},
                'type': { 'required': True,},
            }

            def __init__(self
                    , attributes: _attributes=None            , id: str=None            , type: str=None            ):
                pass
                self.__attributes = attributes
                self.__id = id
                self.__type = type
            
            def _get_attributes(self):
                return self.__attributes
            def _set_attributes(self, value):
                if  not isinstance(value, StorePurchasedCountResp._data._attributes):
                    raise TypeError("attributes must be StorePurchasedCountResp._data._attributes")

                self.__attributes = value
            attributes = property(_get_attributes, _set_attributes)
            
            def _get_id(self):
                return self.__id
            def _set_id(self, value):
                if  not isinstance(value, str):
                    raise TypeError("id must be str")

                self.__id = value
            id = property(_get_id, _set_id)
            
            def _get_type(self):
                return self.__type
            def _set_type(self, value):
                if  not isinstance(value, str):
                    raise TypeError("type must be str")

                self.__type = value
            type = property(_get_type, _set_type)
            

            @staticmethod
            def from_dict(d):
                v = {}
                if "attributes" in d:
                    v["attributes"] = StorePurchasedCountResp._data._attributes.from_dict(d["attributes"]) if hasattr(StorePurchasedCountResp._data._attributes, 'from_dict') else d["attributes"]
                if "id" in d:
                    v["id"] = str.from_dict(d["id"]) if hasattr(str, 'from_dict') else d["id"]
                if "type" in d:
                    v["type"] = str.from_dict(d["type"]) if hasattr(str, 'from_dict') else d["type"]
                return StorePurchasedCountResp._data(**v)


            def as_dict(self):
                d = {}
                if self.__attributes is not None:
                    d['attributes'] = self.__attributes.as_dict() if hasattr(self.__attributes, 'as_dict') else self.__attributes
                if self.__id is not None:
                    d['id'] = self.__id.as_dict() if hasattr(self.__id, 'as_dict') else self.__id
                if self.__type is not None:
                    d['type'] = self.__type.as_dict() if hasattr(self.__type, 'as_dict') else self.__type
                return d

            def __repr__(self):
                return "<Class _data. attributes: {}, id: {}, type: {}>".format(limitedRepr(self.__attributes[:20] if isinstance(self.__attributes, bytes) else self.__attributes), limitedRepr(self.__id[:20] if isinstance(self.__id, bytes) else self.__id), limitedRepr(self.__type[:20] if isinstance(self.__type, bytes) else self.__type))




    _types_map = {
        'data': {'type': _data, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'data': { 'required': True,},
    }

    def __init__(self
            , data: _data=None            ):
        pass
        self.__data = data
    
    def _get_data(self):
        return self.__data
    def _set_data(self, value):
        if  not isinstance(value, StorePurchasedCountResp._data):
            raise TypeError("data must be StorePurchasedCountResp._data")

        self.__data = value
    data = property(_get_data, _set_data)
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "data" in d:
            v["data"] = StorePurchasedCountResp._data.from_dict(d["data"]) if hasattr(StorePurchasedCountResp._data, 'from_dict') else d["data"]
        return StorePurchasedCountResp(**v)


    def as_dict(self):
        d = {}
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        return d

    def __repr__(self):
        return "<Class StorePurchasedCountResp. data: {}>".format(limitedRepr(self.__data[:20] if isinstance(self.__data, bytes) else self.__data))

