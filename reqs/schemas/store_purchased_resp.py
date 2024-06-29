from reprlib import repr as limitedRepr


from typing import List



class StorePurchasedResp:
    class _data:
            class _attributes:
                    class _range:



                            _types_map = {
                                'start': {'type': str, 'subtype': None},
                                'displayable_range': {'type': str, 'subtype': None},
                            }
                            _formats_map = {
                            }
                            _validations_map = {
                                'start': { 'required': True,},
                                'displayable_range': { 'required': True,},
                            }

                            def __init__(self
                                    , start: str=None            , displayable_range: str=None            ):
                                pass
                                self.__start = start
                                self.__displayable_range = displayable_range
                            
                            def _get_start(self):
                                return self.__start
                            def _set_start(self, value):
                                if  not isinstance(value, str):
                                    raise TypeError("start must be str")

                                self.__start = value
                            start = property(_get_start, _set_start)
                            
                            def _get_displayable_range(self):
                                return self.__displayable_range
                            def _set_displayable_range(self, value):
                                if  not isinstance(value, str):
                                    raise TypeError("displayable_range must be str")

                                self.__displayable_range = value
                            displayable_range = property(_get_displayable_range, _set_displayable_range)
                            

                            @staticmethod
                            def from_dict(d):
                                v = {}
                                if "start" in d:
                                    v["start"] = str.from_dict(d["start"]) if hasattr(str, 'from_dict') else d["start"]
                                if "displayable-range" in d:
                                    v["displayable_range"] = str.from_dict(d["displayable-range"]) if hasattr(str, 'from_dict') else d["displayable-range"]
                                return StorePurchasedResp._data._attributes._range(**v)


                            def as_dict(self):
                                d = {}
                                if self.__start is not None:
                                    d['start'] = self.__start.as_dict() if hasattr(self.__start, 'as_dict') else self.__start
                                if self.__displayable_range is not None:
                                    d['displayable-range'] = self.__displayable_range.as_dict() if hasattr(self.__displayable_range, 'as_dict') else self.__displayable_range
                                return d

                            def __repr__(self):
                                return "<Class _range. start: {}, displayable_range: {}>".format(limitedRepr(self.__start[:20] if isinstance(self.__start, bytes) else self.__start), limitedRepr(self.__displayable_range[:20] if isinstance(self.__displayable_range, bytes) else self.__displayable_range))

                    class _purchases:
                            class _items:



                                    _types_map = {
                                        'kind': {'type': str, 'subtype': None},
                                        'displayable_kind': {'type': str, 'subtype': None},
                                        'report_a_problem_url': {'type': str, 'subtype': None},
                                        'artist_name': {'type': str, 'subtype': None},
                                        'item_id': {'type': str, 'subtype': None},
                                        'item_name': {'type': str, 'subtype': None},
                                        'item_url': {'type': str, 'subtype': None},
                                        'seller': {'type': str, 'subtype': None},
                                        'artwork_template_url': {'type': str, 'subtype': None},
                                        'artwork_height': {'type': int, 'subtype': None},
                                        'artwork_width': {'type': int, 'subtype': None},
                                        'is_subscription': {'type': bool, 'subtype': None},
                                        'price': {'type': str, 'subtype': None},
                                        'purchased_from': {'type': str, 'subtype': None},
                                        'partially_refunded': {'type': bool, 'subtype': None},
                                        'refunded': {'type': bool, 'subtype': None},
                                        'cancelled': {'type': bool, 'subtype': None},
                                        'refund_amount': {'type': str, 'subtype': None},
                                        'purchase_date': {'type': str, 'subtype': None},
                                        'is_gift_item': {'type': bool, 'subtype': None},
                                        'item_title': {'type': str, 'subtype': None},
                                        'subscription': {'type': str, 'subtype': None},
                                        'is_invoice_item_name': {'type': bool, 'subtype': None},
                                        'price_from_pli': {'type': str, 'subtype': None},
                                        'quantity': {'type': int, 'subtype': None},
                                    }
                                    _formats_map = {
                                    }
                                    _validations_map = {
                                        'kind': { 'required': True,},
                                        'displayable_kind': { 'required': True,},
                                        'report_a_problem_url': { 'required': True,},
                                        'artist_name': { 'required': True,},
                                        'item_id': { 'required': True,},
                                        'item_name': { 'required': True,},
                                        'item_url': { 'required': True,},
                                        'seller': { 'required': True,},
                                        'artwork_template_url': { 'required': True,},
                                        'artwork_height': { 'required': True,},
                                        'artwork_width': { 'required': True,},
                                        'is_subscription': { 'required': True,},
                                        'price': { 'required': True,},
                                        'purchased_from': { 'required': True,},
                                        'partially_refunded': { 'required': True,},
                                        'refunded': { 'required': True,},
                                        'cancelled': { 'required': True,},
                                        'refund_amount': { 'required': True,},
                                        'purchase_date': { 'required': True,},
                                        'is_gift_item': { 'required': True,},
                                        'item_title': { 'required': True,},
                                        'subscription': { 'required': False,},
                                        'is_invoice_item_name': { 'required': False,},
                                        'price_from_pli': { 'required': False,},
                                        'quantity': { 'required': False,},
                                    }

                                    def __init__(self
                                            , kind: str=None            , displayable_kind: str=None            , report_a_problem_url: str=None            , artist_name: str=None            , item_id: str=None            , item_name: str=None            , item_url: str=None            , seller: str=None            , artwork_template_url: str=None            , artwork_height: int=None            , artwork_width: int=None            , is_subscription: bool=None            , price: str=None            , purchased_from: str=None            , partially_refunded: bool=None            , refunded: bool=None            , cancelled: bool=None            , refund_amount: str=None            , purchase_date: str=None            , is_gift_item: bool=None            , item_title: str=None            , subscription: str=None            , is_invoice_item_name: bool=None            , price_from_pli: str=None            , quantity: int=None            ):
                                        pass
                                        self.__kind = kind
                                        self.__displayable_kind = displayable_kind
                                        self.__report_a_problem_url = report_a_problem_url
                                        self.__artist_name = artist_name
                                        self.__item_id = item_id
                                        self.__item_name = item_name
                                        self.__item_url = item_url
                                        self.__seller = seller
                                        self.__artwork_template_url = artwork_template_url
                                        self.__artwork_height = artwork_height
                                        self.__artwork_width = artwork_width
                                        self.__is_subscription = is_subscription
                                        self.__price = price
                                        self.__purchased_from = purchased_from
                                        self.__partially_refunded = partially_refunded
                                        self.__refunded = refunded
                                        self.__cancelled = cancelled
                                        self.__refund_amount = refund_amount
                                        self.__purchase_date = purchase_date
                                        self.__is_gift_item = is_gift_item
                                        self.__item_title = item_title
                                        self.__subscription = subscription
                                        self.__is_invoice_item_name = is_invoice_item_name
                                        self.__price_from_pli = price_from_pli
                                        self.__quantity = quantity
                                    
                                    def _get_kind(self):
                                        return self.__kind
                                    def _set_kind(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("kind must be str")

                                        self.__kind = value
                                    kind = property(_get_kind, _set_kind)
                                    
                                    def _get_displayable_kind(self):
                                        return self.__displayable_kind
                                    def _set_displayable_kind(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("displayable_kind must be str")

                                        self.__displayable_kind = value
                                    displayable_kind = property(_get_displayable_kind, _set_displayable_kind)
                                    
                                    def _get_report_a_problem_url(self):
                                        return self.__report_a_problem_url
                                    def _set_report_a_problem_url(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("report_a_problem_url must be str")

                                        self.__report_a_problem_url = value
                                    report_a_problem_url = property(_get_report_a_problem_url, _set_report_a_problem_url)
                                    
                                    def _get_artist_name(self):
                                        return self.__artist_name
                                    def _set_artist_name(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("artist_name must be str")

                                        self.__artist_name = value
                                    artist_name = property(_get_artist_name, _set_artist_name)
                                    
                                    def _get_item_id(self):
                                        return self.__item_id
                                    def _set_item_id(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("item_id must be str")

                                        self.__item_id = value
                                    item_id = property(_get_item_id, _set_item_id)
                                    
                                    def _get_item_name(self):
                                        return self.__item_name
                                    def _set_item_name(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("item_name must be str")

                                        self.__item_name = value
                                    item_name = property(_get_item_name, _set_item_name)
                                    
                                    def _get_item_url(self):
                                        return self.__item_url
                                    def _set_item_url(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("item_url must be str")

                                        self.__item_url = value
                                    item_url = property(_get_item_url, _set_item_url)
                                    
                                    def _get_seller(self):
                                        return self.__seller
                                    def _set_seller(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("seller must be str")

                                        self.__seller = value
                                    seller = property(_get_seller, _set_seller)
                                    
                                    def _get_artwork_template_url(self):
                                        return self.__artwork_template_url
                                    def _set_artwork_template_url(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("artwork_template_url must be str")

                                        self.__artwork_template_url = value
                                    artwork_template_url = property(_get_artwork_template_url, _set_artwork_template_url)
                                    
                                    def _get_artwork_height(self):
                                        return self.__artwork_height
                                    def _set_artwork_height(self, value):
                                        if  not isinstance(value, int):
                                            raise TypeError("artwork_height must be int")

                                        self.__artwork_height = value
                                    artwork_height = property(_get_artwork_height, _set_artwork_height)
                                    
                                    def _get_artwork_width(self):
                                        return self.__artwork_width
                                    def _set_artwork_width(self, value):
                                        if  not isinstance(value, int):
                                            raise TypeError("artwork_width must be int")

                                        self.__artwork_width = value
                                    artwork_width = property(_get_artwork_width, _set_artwork_width)
                                    
                                    def _get_is_subscription(self):
                                        return self.__is_subscription
                                    def _set_is_subscription(self, value):
                                        if  not isinstance(value, bool):
                                            raise TypeError("is_subscription must be bool")

                                        self.__is_subscription = value
                                    is_subscription = property(_get_is_subscription, _set_is_subscription)
                                    
                                    def _get_price(self):
                                        return self.__price
                                    def _set_price(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("price must be str")

                                        self.__price = value
                                    price = property(_get_price, _set_price)
                                    
                                    def _get_purchased_from(self):
                                        return self.__purchased_from
                                    def _set_purchased_from(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("purchased_from must be str")

                                        self.__purchased_from = value
                                    purchased_from = property(_get_purchased_from, _set_purchased_from)
                                    
                                    def _get_partially_refunded(self):
                                        return self.__partially_refunded
                                    def _set_partially_refunded(self, value):
                                        if  not isinstance(value, bool):
                                            raise TypeError("partially_refunded must be bool")

                                        self.__partially_refunded = value
                                    partially_refunded = property(_get_partially_refunded, _set_partially_refunded)
                                    
                                    def _get_refunded(self):
                                        return self.__refunded
                                    def _set_refunded(self, value):
                                        if  not isinstance(value, bool):
                                            raise TypeError("refunded must be bool")

                                        self.__refunded = value
                                    refunded = property(_get_refunded, _set_refunded)
                                    
                                    def _get_cancelled(self):
                                        return self.__cancelled
                                    def _set_cancelled(self, value):
                                        if  not isinstance(value, bool):
                                            raise TypeError("cancelled must be bool")

                                        self.__cancelled = value
                                    cancelled = property(_get_cancelled, _set_cancelled)
                                    
                                    def _get_refund_amount(self):
                                        return self.__refund_amount
                                    def _set_refund_amount(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("refund_amount must be str")

                                        self.__refund_amount = value
                                    refund_amount = property(_get_refund_amount, _set_refund_amount)
                                    
                                    def _get_purchase_date(self):
                                        return self.__purchase_date
                                    def _set_purchase_date(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("purchase_date must be str")

                                        self.__purchase_date = value
                                    purchase_date = property(_get_purchase_date, _set_purchase_date)
                                    
                                    def _get_is_gift_item(self):
                                        return self.__is_gift_item
                                    def _set_is_gift_item(self, value):
                                        if  not isinstance(value, bool):
                                            raise TypeError("is_gift_item must be bool")

                                        self.__is_gift_item = value
                                    is_gift_item = property(_get_is_gift_item, _set_is_gift_item)
                                    
                                    def _get_item_title(self):
                                        return self.__item_title
                                    def _set_item_title(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("item_title must be str")

                                        self.__item_title = value
                                    item_title = property(_get_item_title, _set_item_title)
                                    
                                    def _get_subscription(self):
                                        return self.__subscription
                                    def _set_subscription(self, value):
                                        if value is not None and  not isinstance(value, str):
                                            raise TypeError("subscription must be str")

                                        self.__subscription = value
                                    subscription = property(_get_subscription, _set_subscription)
                                    
                                    def _get_is_invoice_item_name(self):
                                        return self.__is_invoice_item_name
                                    def _set_is_invoice_item_name(self, value):
                                        if value is not None and  not isinstance(value, bool):
                                            raise TypeError("is_invoice_item_name must be bool")

                                        self.__is_invoice_item_name = value
                                    is_invoice_item_name = property(_get_is_invoice_item_name, _set_is_invoice_item_name)
                                    
                                    def _get_price_from_pli(self):
                                        return self.__price_from_pli
                                    def _set_price_from_pli(self, value):
                                        if value is not None and  not isinstance(value, str):
                                            raise TypeError("price_from_pli must be str")

                                        self.__price_from_pli = value
                                    price_from_pli = property(_get_price_from_pli, _set_price_from_pli)
                                    
                                    def _get_quantity(self):
                                        return self.__quantity
                                    def _set_quantity(self, value):
                                        if value is not None and  not isinstance(value, int):
                                            raise TypeError("quantity must be int")

                                        self.__quantity = value
                                    quantity = property(_get_quantity, _set_quantity)
                                    

                                    @staticmethod
                                    def from_dict(d):
                                        v = {}
                                        if "kind" in d:
                                            v["kind"] = str.from_dict(d["kind"]) if hasattr(str, 'from_dict') else d["kind"]
                                        if "displayable-kind" in d:
                                            v["displayable_kind"] = str.from_dict(d["displayable-kind"]) if hasattr(str, 'from_dict') else d["displayable-kind"]
                                        if "report-a-problem-url" in d:
                                            v["report_a_problem_url"] = str.from_dict(d["report-a-problem-url"]) if hasattr(str, 'from_dict') else d["report-a-problem-url"]
                                        if "artist-name" in d:
                                            v["artist_name"] = str.from_dict(d["artist-name"]) if hasattr(str, 'from_dict') else d["artist-name"]
                                        if "item-id" in d:
                                            v["item_id"] = str.from_dict(d["item-id"]) if hasattr(str, 'from_dict') else d["item-id"]
                                        if "item-name" in d:
                                            v["item_name"] = str.from_dict(d["item-name"]) if hasattr(str, 'from_dict') else d["item-name"]
                                        if "item-url" in d:
                                            v["item_url"] = str.from_dict(d["item-url"]) if hasattr(str, 'from_dict') else d["item-url"]
                                        if "seller" in d:
                                            v["seller"] = str.from_dict(d["seller"]) if hasattr(str, 'from_dict') else d["seller"]
                                        if "artwork-template-url" in d:
                                            v["artwork_template_url"] = str.from_dict(d["artwork-template-url"]) if hasattr(str, 'from_dict') else d["artwork-template-url"]
                                        if "artwork-height" in d:
                                            v["artwork_height"] = int.from_dict(d["artwork-height"]) if hasattr(int, 'from_dict') else d["artwork-height"]
                                        if "artwork-width" in d:
                                            v["artwork_width"] = int.from_dict(d["artwork-width"]) if hasattr(int, 'from_dict') else d["artwork-width"]
                                        if "is-subscription" in d:
                                            v["is_subscription"] = bool.from_dict(d["is-subscription"]) if hasattr(bool, 'from_dict') else d["is-subscription"]
                                        if "price" in d:
                                            v["price"] = str.from_dict(d["price"]) if hasattr(str, 'from_dict') else d["price"]
                                        if "purchased-from" in d:
                                            v["purchased_from"] = str.from_dict(d["purchased-from"]) if hasattr(str, 'from_dict') else d["purchased-from"]
                                        if "partially-refunded" in d:
                                            v["partially_refunded"] = bool.from_dict(d["partially-refunded"]) if hasattr(bool, 'from_dict') else d["partially-refunded"]
                                        if "refunded" in d:
                                            v["refunded"] = bool.from_dict(d["refunded"]) if hasattr(bool, 'from_dict') else d["refunded"]
                                        if "cancelled" in d:
                                            v["cancelled"] = bool.from_dict(d["cancelled"]) if hasattr(bool, 'from_dict') else d["cancelled"]
                                        if "refund-amount" in d:
                                            v["refund_amount"] = str.from_dict(d["refund-amount"]) if hasattr(str, 'from_dict') else d["refund-amount"]
                                        if "purchase-date" in d:
                                            v["purchase_date"] = str.from_dict(d["purchase-date"]) if hasattr(str, 'from_dict') else d["purchase-date"]
                                        if "is-gift-item" in d:
                                            v["is_gift_item"] = bool.from_dict(d["is-gift-item"]) if hasattr(bool, 'from_dict') else d["is-gift-item"]
                                        if "item-title" in d:
                                            v["item_title"] = str.from_dict(d["item-title"]) if hasattr(str, 'from_dict') else d["item-title"]
                                        if "subscription" in d:
                                            v["subscription"] = str.from_dict(d["subscription"]) if hasattr(str, 'from_dict') else d["subscription"]
                                        if "is-invoice-item-name" in d:
                                            v["is_invoice_item_name"] = bool.from_dict(d["is-invoice-item-name"]) if hasattr(bool, 'from_dict') else d["is-invoice-item-name"]
                                        if "price-from-pli" in d:
                                            v["price_from_pli"] = str.from_dict(d["price-from-pli"]) if hasattr(str, 'from_dict') else d["price-from-pli"]
                                        if "quantity" in d:
                                            v["quantity"] = int.from_dict(d["quantity"]) if hasattr(int, 'from_dict') else d["quantity"]
                                        return StorePurchasedResp._data._attributes._purchases._items(**v)


                                    def as_dict(self):
                                        d = {}
                                        if self.__kind is not None:
                                            d['kind'] = self.__kind.as_dict() if hasattr(self.__kind, 'as_dict') else self.__kind
                                        if self.__displayable_kind is not None:
                                            d['displayable-kind'] = self.__displayable_kind.as_dict() if hasattr(self.__displayable_kind, 'as_dict') else self.__displayable_kind
                                        if self.__report_a_problem_url is not None:
                                            d['report-a-problem-url'] = self.__report_a_problem_url.as_dict() if hasattr(self.__report_a_problem_url, 'as_dict') else self.__report_a_problem_url
                                        if self.__artist_name is not None:
                                            d['artist-name'] = self.__artist_name.as_dict() if hasattr(self.__artist_name, 'as_dict') else self.__artist_name
                                        if self.__item_id is not None:
                                            d['item-id'] = self.__item_id.as_dict() if hasattr(self.__item_id, 'as_dict') else self.__item_id
                                        if self.__item_name is not None:
                                            d['item-name'] = self.__item_name.as_dict() if hasattr(self.__item_name, 'as_dict') else self.__item_name
                                        if self.__item_url is not None:
                                            d['item-url'] = self.__item_url.as_dict() if hasattr(self.__item_url, 'as_dict') else self.__item_url
                                        if self.__seller is not None:
                                            d['seller'] = self.__seller.as_dict() if hasattr(self.__seller, 'as_dict') else self.__seller
                                        if self.__artwork_template_url is not None:
                                            d['artwork-template-url'] = self.__artwork_template_url.as_dict() if hasattr(self.__artwork_template_url, 'as_dict') else self.__artwork_template_url
                                        if self.__artwork_height is not None:
                                            d['artwork-height'] = self.__artwork_height.as_dict() if hasattr(self.__artwork_height, 'as_dict') else self.__artwork_height
                                        if self.__artwork_width is not None:
                                            d['artwork-width'] = self.__artwork_width.as_dict() if hasattr(self.__artwork_width, 'as_dict') else self.__artwork_width
                                        if self.__is_subscription is not None:
                                            d['is-subscription'] = self.__is_subscription.as_dict() if hasattr(self.__is_subscription, 'as_dict') else self.__is_subscription
                                        if self.__price is not None:
                                            d['price'] = self.__price.as_dict() if hasattr(self.__price, 'as_dict') else self.__price
                                        if self.__purchased_from is not None:
                                            d['purchased-from'] = self.__purchased_from.as_dict() if hasattr(self.__purchased_from, 'as_dict') else self.__purchased_from
                                        if self.__partially_refunded is not None:
                                            d['partially-refunded'] = self.__partially_refunded.as_dict() if hasattr(self.__partially_refunded, 'as_dict') else self.__partially_refunded
                                        if self.__refunded is not None:
                                            d['refunded'] = self.__refunded.as_dict() if hasattr(self.__refunded, 'as_dict') else self.__refunded
                                        if self.__cancelled is not None:
                                            d['cancelled'] = self.__cancelled.as_dict() if hasattr(self.__cancelled, 'as_dict') else self.__cancelled
                                        if self.__refund_amount is not None:
                                            d['refund-amount'] = self.__refund_amount.as_dict() if hasattr(self.__refund_amount, 'as_dict') else self.__refund_amount
                                        if self.__purchase_date is not None:
                                            d['purchase-date'] = self.__purchase_date.as_dict() if hasattr(self.__purchase_date, 'as_dict') else self.__purchase_date
                                        if self.__is_gift_item is not None:
                                            d['is-gift-item'] = self.__is_gift_item.as_dict() if hasattr(self.__is_gift_item, 'as_dict') else self.__is_gift_item
                                        if self.__item_title is not None:
                                            d['item-title'] = self.__item_title.as_dict() if hasattr(self.__item_title, 'as_dict') else self.__item_title
                                        if self.__subscription is not None:
                                            d['subscription'] = self.__subscription.as_dict() if hasattr(self.__subscription, 'as_dict') else self.__subscription
                                        if self.__is_invoice_item_name is not None:
                                            d['is-invoice-item-name'] = self.__is_invoice_item_name.as_dict() if hasattr(self.__is_invoice_item_name, 'as_dict') else self.__is_invoice_item_name
                                        if self.__price_from_pli is not None:
                                            d['price-from-pli'] = self.__price_from_pli.as_dict() if hasattr(self.__price_from_pli, 'as_dict') else self.__price_from_pli
                                        if self.__quantity is not None:
                                            d['quantity'] = self.__quantity.as_dict() if hasattr(self.__quantity, 'as_dict') else self.__quantity
                                        return d

                                    def __repr__(self):
                                        return "<Class _items. kind: {}, displayable_kind: {}, report_a_problem_url: {}, artist_name: {}, item_id: {}, item_name: {}, item_url: {}, seller: {}, artwork_template_url: {}, artwork_height: {}, artwork_width: {}, is_subscription: {}, price: {}, purchased_from: {}, partially_refunded: {}, refunded: {}, cancelled: {}, refund_amount: {}, purchase_date: {}, is_gift_item: {}, item_title: {}, subscription: {}, is_invoice_item_name: {}, price_from_pli: {}, quantity: {}>".format(limitedRepr(self.__kind[:20] if isinstance(self.__kind, bytes) else self.__kind), limitedRepr(self.__displayable_kind[:20] if isinstance(self.__displayable_kind, bytes) else self.__displayable_kind), limitedRepr(self.__report_a_problem_url[:20] if isinstance(self.__report_a_problem_url, bytes) else self.__report_a_problem_url), limitedRepr(self.__artist_name[:20] if isinstance(self.__artist_name, bytes) else self.__artist_name), limitedRepr(self.__item_id[:20] if isinstance(self.__item_id, bytes) else self.__item_id), limitedRepr(self.__item_name[:20] if isinstance(self.__item_name, bytes) else self.__item_name), limitedRepr(self.__item_url[:20] if isinstance(self.__item_url, bytes) else self.__item_url), limitedRepr(self.__seller[:20] if isinstance(self.__seller, bytes) else self.__seller), limitedRepr(self.__artwork_template_url[:20] if isinstance(self.__artwork_template_url, bytes) else self.__artwork_template_url), limitedRepr(self.__artwork_height[:20] if isinstance(self.__artwork_height, bytes) else self.__artwork_height), limitedRepr(self.__artwork_width[:20] if isinstance(self.__artwork_width, bytes) else self.__artwork_width), limitedRepr(self.__is_subscription[:20] if isinstance(self.__is_subscription, bytes) else self.__is_subscription), limitedRepr(self.__price[:20] if isinstance(self.__price, bytes) else self.__price), limitedRepr(self.__purchased_from[:20] if isinstance(self.__purchased_from, bytes) else self.__purchased_from), limitedRepr(self.__partially_refunded[:20] if isinstance(self.__partially_refunded, bytes) else self.__partially_refunded), limitedRepr(self.__refunded[:20] if isinstance(self.__refunded, bytes) else self.__refunded), limitedRepr(self.__cancelled[:20] if isinstance(self.__cancelled, bytes) else self.__cancelled), limitedRepr(self.__refund_amount[:20] if isinstance(self.__refund_amount, bytes) else self.__refund_amount), limitedRepr(self.__purchase_date[:20] if isinstance(self.__purchase_date, bytes) else self.__purchase_date), limitedRepr(self.__is_gift_item[:20] if isinstance(self.__is_gift_item, bytes) else self.__is_gift_item), limitedRepr(self.__item_title[:20] if isinstance(self.__item_title, bytes) else self.__item_title), limitedRepr(self.__subscription[:20] if isinstance(self.__subscription, bytes) else self.__subscription), limitedRepr(self.__is_invoice_item_name[:20] if isinstance(self.__is_invoice_item_name, bytes) else self.__is_invoice_item_name), limitedRepr(self.__price_from_pli[:20] if isinstance(self.__price_from_pli, bytes) else self.__price_from_pli), limitedRepr(self.__quantity[:20] if isinstance(self.__quantity, bytes) else self.__quantity))

                            class _billed_to:
                                    class _methods:



                                            _types_map = {
                                                'amount': {'type': str, 'subtype': None},
                                                'name': {'type': str, 'subtype': None},
                                            }
                                            _formats_map = {
                                            }
                                            _validations_map = {
                                                'amount': { 'required': True,},
                                                'name': { 'required': True,},
                                            }

                                            def __init__(self
                                                    , amount: str=None            , name: str=None            ):
                                                pass
                                                self.__amount = amount
                                                self.__name = name
                                            
                                            def _get_amount(self):
                                                return self.__amount
                                            def _set_amount(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("amount must be str")

                                                self.__amount = value
                                            amount = property(_get_amount, _set_amount)
                                            
                                            def _get_name(self):
                                                return self.__name
                                            def _set_name(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("name must be str")

                                                self.__name = value
                                            name = property(_get_name, _set_name)
                                            

                                            @staticmethod
                                            def from_dict(d):
                                                v = {}
                                                if "amount" in d:
                                                    v["amount"] = str.from_dict(d["amount"]) if hasattr(str, 'from_dict') else d["amount"]
                                                if "name" in d:
                                                    v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                                                return StorePurchasedResp._data._attributes._purchases._billed_to._methods(**v)


                                            def as_dict(self):
                                                d = {}
                                                if self.__amount is not None:
                                                    d['amount'] = self.__amount.as_dict() if hasattr(self.__amount, 'as_dict') else self.__amount
                                                if self.__name is not None:
                                                    d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                                                return d

                                            def __repr__(self):
                                                return "<Class _methods. amount: {}, name: {}>".format(limitedRepr(self.__amount[:20] if isinstance(self.__amount, bytes) else self.__amount), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name))

                                    class _address:



                                            _types_map = {
                                                'addressOfficialCity': {'type': str, 'subtype': None},
                                                'addressOfficialCountryCode': {'type': str, 'subtype': None},
                                                'addressOfficialStateProvince': {'type': str, 'subtype': None},
                                                'addressOfficialLineFirst': {'type': str, 'subtype': None},
                                                'addressOfficialLineSecond': {'type': str, 'subtype': None},
                                                'addressOfficialLineThird': {'type': str, 'subtype': None},
                                                'addressOfficialPostalCode': {'type': str, 'subtype': None},
                                                'billingFirstName': {'type': str, 'subtype': None},
                                                'billingLastName': {'type': str, 'subtype': None},
                                                'billingNamePrefix': {'type': str, 'subtype': None},
                                            }
                                            _formats_map = {
                                            }
                                            _validations_map = {
                                                'addressOfficialCity': { 'required': True,},
                                                'addressOfficialCountryCode': { 'required': True,},
                                                'addressOfficialStateProvince': { 'required': True,},
                                                'addressOfficialLineFirst': { 'required': True,},
                                                'addressOfficialLineSecond': { 'required': True,},
                                                'addressOfficialLineThird': { 'required': True,},
                                                'addressOfficialPostalCode': { 'required': True,},
                                                'billingFirstName': { 'required': True,},
                                                'billingLastName': { 'required': True,},
                                                'billingNamePrefix': { 'required': True,},
                                            }

                                            def __init__(self
                                                    , addressOfficialCity: str=None            , addressOfficialCountryCode: str=None            , addressOfficialStateProvince: str=None            , addressOfficialLineFirst: str=None            , addressOfficialLineSecond: str=None            , addressOfficialLineThird: str=None            , addressOfficialPostalCode: str=None            , billingFirstName: str=None            , billingLastName: str=None            , billingNamePrefix: str=None            ):
                                                pass
                                                self.__addressOfficialCity = addressOfficialCity
                                                self.__addressOfficialCountryCode = addressOfficialCountryCode
                                                self.__addressOfficialStateProvince = addressOfficialStateProvince
                                                self.__addressOfficialLineFirst = addressOfficialLineFirst
                                                self.__addressOfficialLineSecond = addressOfficialLineSecond
                                                self.__addressOfficialLineThird = addressOfficialLineThird
                                                self.__addressOfficialPostalCode = addressOfficialPostalCode
                                                self.__billingFirstName = billingFirstName
                                                self.__billingLastName = billingLastName
                                                self.__billingNamePrefix = billingNamePrefix
                                            
                                            def _get_addressOfficialCity(self):
                                                return self.__addressOfficialCity
                                            def _set_addressOfficialCity(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("addressOfficialCity must be str")

                                                self.__addressOfficialCity = value
                                            addressOfficialCity = property(_get_addressOfficialCity, _set_addressOfficialCity)
                                            
                                            def _get_addressOfficialCountryCode(self):
                                                return self.__addressOfficialCountryCode
                                            def _set_addressOfficialCountryCode(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("addressOfficialCountryCode must be str")

                                                self.__addressOfficialCountryCode = value
                                            addressOfficialCountryCode = property(_get_addressOfficialCountryCode, _set_addressOfficialCountryCode)
                                            
                                            def _get_addressOfficialStateProvince(self):
                                                return self.__addressOfficialStateProvince
                                            def _set_addressOfficialStateProvince(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("addressOfficialStateProvince must be str")

                                                self.__addressOfficialStateProvince = value
                                            addressOfficialStateProvince = property(_get_addressOfficialStateProvince, _set_addressOfficialStateProvince)
                                            
                                            def _get_addressOfficialLineFirst(self):
                                                return self.__addressOfficialLineFirst
                                            def _set_addressOfficialLineFirst(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("addressOfficialLineFirst must be str")

                                                self.__addressOfficialLineFirst = value
                                            addressOfficialLineFirst = property(_get_addressOfficialLineFirst, _set_addressOfficialLineFirst)
                                            
                                            def _get_addressOfficialLineSecond(self):
                                                return self.__addressOfficialLineSecond
                                            def _set_addressOfficialLineSecond(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("addressOfficialLineSecond must be str")

                                                self.__addressOfficialLineSecond = value
                                            addressOfficialLineSecond = property(_get_addressOfficialLineSecond, _set_addressOfficialLineSecond)
                                            
                                            def _get_addressOfficialLineThird(self):
                                                return self.__addressOfficialLineThird
                                            def _set_addressOfficialLineThird(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("addressOfficialLineThird must be str")

                                                self.__addressOfficialLineThird = value
                                            addressOfficialLineThird = property(_get_addressOfficialLineThird, _set_addressOfficialLineThird)
                                            
                                            def _get_addressOfficialPostalCode(self):
                                                return self.__addressOfficialPostalCode
                                            def _set_addressOfficialPostalCode(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("addressOfficialPostalCode must be str")

                                                self.__addressOfficialPostalCode = value
                                            addressOfficialPostalCode = property(_get_addressOfficialPostalCode, _set_addressOfficialPostalCode)
                                            
                                            def _get_billingFirstName(self):
                                                return self.__billingFirstName
                                            def _set_billingFirstName(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("billingFirstName must be str")

                                                self.__billingFirstName = value
                                            billingFirstName = property(_get_billingFirstName, _set_billingFirstName)
                                            
                                            def _get_billingLastName(self):
                                                return self.__billingLastName
                                            def _set_billingLastName(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("billingLastName must be str")

                                                self.__billingLastName = value
                                            billingLastName = property(_get_billingLastName, _set_billingLastName)
                                            
                                            def _get_billingNamePrefix(self):
                                                return self.__billingNamePrefix
                                            def _set_billingNamePrefix(self, value):
                                                if  not isinstance(value, str):
                                                    raise TypeError("billingNamePrefix must be str")

                                                self.__billingNamePrefix = value
                                            billingNamePrefix = property(_get_billingNamePrefix, _set_billingNamePrefix)
                                            

                                            @staticmethod
                                            def from_dict(d):
                                                v = {}
                                                if "addressOfficialCity" in d:
                                                    v["addressOfficialCity"] = str.from_dict(d["addressOfficialCity"]) if hasattr(str, 'from_dict') else d["addressOfficialCity"]
                                                if "addressOfficialCountryCode" in d:
                                                    v["addressOfficialCountryCode"] = str.from_dict(d["addressOfficialCountryCode"]) if hasattr(str, 'from_dict') else d["addressOfficialCountryCode"]
                                                if "addressOfficialStateProvince" in d:
                                                    v["addressOfficialStateProvince"] = str.from_dict(d["addressOfficialStateProvince"]) if hasattr(str, 'from_dict') else d["addressOfficialStateProvince"]
                                                if "addressOfficialLineFirst" in d:
                                                    v["addressOfficialLineFirst"] = str.from_dict(d["addressOfficialLineFirst"]) if hasattr(str, 'from_dict') else d["addressOfficialLineFirst"]
                                                if "addressOfficialLineSecond" in d:
                                                    v["addressOfficialLineSecond"] = str.from_dict(d["addressOfficialLineSecond"]) if hasattr(str, 'from_dict') else d["addressOfficialLineSecond"]
                                                if "addressOfficialLineThird" in d:
                                                    v["addressOfficialLineThird"] = str.from_dict(d["addressOfficialLineThird"]) if hasattr(str, 'from_dict') else d["addressOfficialLineThird"]
                                                if "addressOfficialPostalCode" in d:
                                                    v["addressOfficialPostalCode"] = str.from_dict(d["addressOfficialPostalCode"]) if hasattr(str, 'from_dict') else d["addressOfficialPostalCode"]
                                                if "billingFirstName" in d:
                                                    v["billingFirstName"] = str.from_dict(d["billingFirstName"]) if hasattr(str, 'from_dict') else d["billingFirstName"]
                                                if "billingLastName" in d:
                                                    v["billingLastName"] = str.from_dict(d["billingLastName"]) if hasattr(str, 'from_dict') else d["billingLastName"]
                                                if "billingNamePrefix" in d:
                                                    v["billingNamePrefix"] = str.from_dict(d["billingNamePrefix"]) if hasattr(str, 'from_dict') else d["billingNamePrefix"]
                                                return StorePurchasedResp._data._attributes._purchases._billed_to._address(**v)


                                            def as_dict(self):
                                                d = {}
                                                if self.__addressOfficialCity is not None:
                                                    d['addressOfficialCity'] = self.__addressOfficialCity.as_dict() if hasattr(self.__addressOfficialCity, 'as_dict') else self.__addressOfficialCity
                                                if self.__addressOfficialCountryCode is not None:
                                                    d['addressOfficialCountryCode'] = self.__addressOfficialCountryCode.as_dict() if hasattr(self.__addressOfficialCountryCode, 'as_dict') else self.__addressOfficialCountryCode
                                                if self.__addressOfficialStateProvince is not None:
                                                    d['addressOfficialStateProvince'] = self.__addressOfficialStateProvince.as_dict() if hasattr(self.__addressOfficialStateProvince, 'as_dict') else self.__addressOfficialStateProvince
                                                if self.__addressOfficialLineFirst is not None:
                                                    d['addressOfficialLineFirst'] = self.__addressOfficialLineFirst.as_dict() if hasattr(self.__addressOfficialLineFirst, 'as_dict') else self.__addressOfficialLineFirst
                                                if self.__addressOfficialLineSecond is not None:
                                                    d['addressOfficialLineSecond'] = self.__addressOfficialLineSecond.as_dict() if hasattr(self.__addressOfficialLineSecond, 'as_dict') else self.__addressOfficialLineSecond
                                                if self.__addressOfficialLineThird is not None:
                                                    d['addressOfficialLineThird'] = self.__addressOfficialLineThird.as_dict() if hasattr(self.__addressOfficialLineThird, 'as_dict') else self.__addressOfficialLineThird
                                                if self.__addressOfficialPostalCode is not None:
                                                    d['addressOfficialPostalCode'] = self.__addressOfficialPostalCode.as_dict() if hasattr(self.__addressOfficialPostalCode, 'as_dict') else self.__addressOfficialPostalCode
                                                if self.__billingFirstName is not None:
                                                    d['billingFirstName'] = self.__billingFirstName.as_dict() if hasattr(self.__billingFirstName, 'as_dict') else self.__billingFirstName
                                                if self.__billingLastName is not None:
                                                    d['billingLastName'] = self.__billingLastName.as_dict() if hasattr(self.__billingLastName, 'as_dict') else self.__billingLastName
                                                if self.__billingNamePrefix is not None:
                                                    d['billingNamePrefix'] = self.__billingNamePrefix.as_dict() if hasattr(self.__billingNamePrefix, 'as_dict') else self.__billingNamePrefix
                                                return d

                                            def __repr__(self):
                                                return "<Class _address. addressOfficialCity: {}, addressOfficialCountryCode: {}, addressOfficialStateProvince: {}, addressOfficialLineFirst: {}, addressOfficialLineSecond: {}, addressOfficialLineThird: {}, addressOfficialPostalCode: {}, billingFirstName: {}, billingLastName: {}, billingNamePrefix: {}>".format(limitedRepr(self.__addressOfficialCity[:20] if isinstance(self.__addressOfficialCity, bytes) else self.__addressOfficialCity), limitedRepr(self.__addressOfficialCountryCode[:20] if isinstance(self.__addressOfficialCountryCode, bytes) else self.__addressOfficialCountryCode), limitedRepr(self.__addressOfficialStateProvince[:20] if isinstance(self.__addressOfficialStateProvince, bytes) else self.__addressOfficialStateProvince), limitedRepr(self.__addressOfficialLineFirst[:20] if isinstance(self.__addressOfficialLineFirst, bytes) else self.__addressOfficialLineFirst), limitedRepr(self.__addressOfficialLineSecond[:20] if isinstance(self.__addressOfficialLineSecond, bytes) else self.__addressOfficialLineSecond), limitedRepr(self.__addressOfficialLineThird[:20] if isinstance(self.__addressOfficialLineThird, bytes) else self.__addressOfficialLineThird), limitedRepr(self.__addressOfficialPostalCode[:20] if isinstance(self.__addressOfficialPostalCode, bytes) else self.__addressOfficialPostalCode), limitedRepr(self.__billingFirstName[:20] if isinstance(self.__billingFirstName, bytes) else self.__billingFirstName), limitedRepr(self.__billingLastName[:20] if isinstance(self.__billingLastName, bytes) else self.__billingLastName), limitedRepr(self.__billingNamePrefix[:20] if isinstance(self.__billingNamePrefix, bytes) else self.__billingNamePrefix))




                                    _types_map = {
                                        'address': {'type': _address, 'subtype': None},
                                        'email': {'type': str, 'subtype': None},
                                        'is_vat': {'type': bool, 'subtype': None},
                                        'receipt_label': {'type': str, 'subtype': None},
                                        'methods': {'type': list, 'subtype': _methods},
                                    }
                                    _formats_map = {
                                    }
                                    _validations_map = {
                                        'address': { 'required': True,},
                                        'email': { 'required': True,},
                                        'is_vat': { 'required': True,},
                                        'receipt_label': { 'required': True,},
                                        'methods': { 'required': False,},
                                    }

                                    def __init__(self
                                            , address: _address=None            , email: str=None            , is_vat: bool=None            , receipt_label: str=None            , methods: List[_methods]
                                =None            ):
                                        pass
                                        self.__address = address
                                        self.__email = email
                                        self.__is_vat = is_vat
                                        self.__receipt_label = receipt_label
                                        self.__methods = methods
                                    
                                    def _get_address(self):
                                        return self.__address
                                    def _set_address(self, value):
                                        if  not isinstance(value, StorePurchasedResp._data._attributes._purchases._billed_to._address):
                                            raise TypeError("address must be StorePurchasedResp._data._attributes._purchases._billed_to._address")

                                        self.__address = value
                                    address = property(_get_address, _set_address)
                                    
                                    def _get_email(self):
                                        return self.__email
                                    def _set_email(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("email must be str")

                                        self.__email = value
                                    email = property(_get_email, _set_email)
                                    
                                    def _get_is_vat(self):
                                        return self.__is_vat
                                    def _set_is_vat(self, value):
                                        if  not isinstance(value, bool):
                                            raise TypeError("is_vat must be bool")

                                        self.__is_vat = value
                                    is_vat = property(_get_is_vat, _set_is_vat)
                                    
                                    def _get_receipt_label(self):
                                        return self.__receipt_label
                                    def _set_receipt_label(self, value):
                                        if  not isinstance(value, str):
                                            raise TypeError("receipt_label must be str")

                                        self.__receipt_label = value
                                    receipt_label = property(_get_receipt_label, _set_receipt_label)
                                    
                                    def _get_methods(self):
                                        return self.__methods
                                    def _set_methods(self, value):
                                        if value is not None and  not isinstance(value, list):
                                            raise TypeError("methods must be list")
                                        if value is not None and  not all(isinstance(i, StorePurchasedResp._data._attributes._purchases._billed_to._methods) for i in value):
                                            raise TypeError("methods list values must be StorePurchasedResp._data._attributes._purchases._billed_to._methods")

                                        self.__methods = value
                                    methods = property(_get_methods, _set_methods)
                                    

                                    @staticmethod
                                    def from_dict(d):
                                        v = {}
                                        if "address" in d:
                                            v["address"] = StorePurchasedResp._data._attributes._purchases._billed_to._address.from_dict(d["address"]) if hasattr(StorePurchasedResp._data._attributes._purchases._billed_to._address, 'from_dict') else d["address"]
                                        if "email" in d:
                                            v["email"] = str.from_dict(d["email"]) if hasattr(str, 'from_dict') else d["email"]
                                        if "is-vat" in d:
                                            v["is_vat"] = bool.from_dict(d["is-vat"]) if hasattr(bool, 'from_dict') else d["is-vat"]
                                        if "receipt-label" in d:
                                            v["receipt_label"] = str.from_dict(d["receipt-label"]) if hasattr(str, 'from_dict') else d["receipt-label"]
                                        if "methods" in d:
                                            v["methods"] = [StorePurchasedResp._data._attributes._purchases._billed_to._methods.from_dict(p) if hasattr(StorePurchasedResp._data._attributes._purchases._billed_to._methods, 'from_dict') else p for p in d["methods"]]
                                        return StorePurchasedResp._data._attributes._purchases._billed_to(**v)


                                    def as_dict(self):
                                        d = {}
                                        if self.__address is not None:
                                            d['address'] = self.__address.as_dict() if hasattr(self.__address, 'as_dict') else self.__address
                                        if self.__email is not None:
                                            d['email'] = self.__email.as_dict() if hasattr(self.__email, 'as_dict') else self.__email
                                        if self.__is_vat is not None:
                                            d['is-vat'] = self.__is_vat.as_dict() if hasattr(self.__is_vat, 'as_dict') else self.__is_vat
                                        if self.__receipt_label is not None:
                                            d['receipt-label'] = self.__receipt_label.as_dict() if hasattr(self.__receipt_label, 'as_dict') else self.__receipt_label
                                        if self.__methods is not None:
                                            d['methods'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__methods]
                                        return d

                                    def __repr__(self):
                                        return "<Class _billed_to. address: {}, email: {}, is_vat: {}, receipt_label: {}, methods: {}>".format(limitedRepr(self.__address[:20] if isinstance(self.__address, bytes) else self.__address), limitedRepr(self.__email[:20] if isinstance(self.__email, bytes) else self.__email), limitedRepr(self.__is_vat[:20] if isinstance(self.__is_vat, bytes) else self.__is_vat), limitedRepr(self.__receipt_label[:20] if isinstance(self.__receipt_label, bytes) else self.__receipt_label), limitedRepr(self.__methods[:20] if isinstance(self.__methods, bytes) else self.__methods))




                            _types_map = {
                                'billed_to': {'type': _billed_to, 'subtype': None},
                                'id': {'type': int, 'subtype': None},
                                'invoice_date': {'type': str, 'subtype': None},
                                'items': {'type': list, 'subtype': _items},
                                'order_id': {'type': str, 'subtype': None},
                                'pending': {'type': bool, 'subtype': None},
                                'sub_total': {'type': str, 'subtype': None},
                                'tax': {'type': str, 'subtype': None},
                                'total': {'type': str, 'subtype': None},
                                'from_email_invoice': {'type': bool, 'subtype': None},
                                'is_chargeback': {'type': bool, 'subtype': None},
                                'show_tax': {'type': bool, 'subtype': None},
                                'show_sub_total': {'type': bool, 'subtype': None},
                                'can_be_cleared_with_store_credit': {'type': bool, 'subtype': None},
                                'document_number': {'type': str, 'subtype': None},
                            }
                            _formats_map = {
                            }
                            _validations_map = {
                                'billed_to': { 'required': True,},
                                'id': { 'required': True,},
                                'invoice_date': { 'required': True,},
                                'items': { 'required': True,},
                                'order_id': { 'required': True,},
                                'pending': { 'required': True,},
                                'sub_total': { 'required': True,},
                                'tax': { 'required': True,},
                                'total': { 'required': True,},
                                'from_email_invoice': { 'required': True,},
                                'is_chargeback': { 'required': True,},
                                'show_tax': { 'required': True,},
                                'show_sub_total': { 'required': True,},
                                'can_be_cleared_with_store_credit': { 'required': True,},
                                'document_number': { 'required': False,},
                            }

                            def __init__(self
                                    , billed_to: _billed_to=None            , id: int=None            , invoice_date: str=None            , items: List[_items]
                        =None            , order_id: str=None            , pending: bool=None            , sub_total: str=None            , tax: str=None            , total: str=None            , from_email_invoice: bool=None            , is_chargeback: bool=None            , show_tax: bool=None            , show_sub_total: bool=None            , can_be_cleared_with_store_credit: bool=None            , document_number: str=None            ):
                                pass
                                self.__billed_to = billed_to
                                self.__id = id
                                self.__invoice_date = invoice_date
                                self.__items = items
                                self.__order_id = order_id
                                self.__pending = pending
                                self.__sub_total = sub_total
                                self.__tax = tax
                                self.__total = total
                                self.__from_email_invoice = from_email_invoice
                                self.__is_chargeback = is_chargeback
                                self.__show_tax = show_tax
                                self.__show_sub_total = show_sub_total
                                self.__can_be_cleared_with_store_credit = can_be_cleared_with_store_credit
                                self.__document_number = document_number
                            
                            def _get_billed_to(self):
                                return self.__billed_to
                            def _set_billed_to(self, value):
                                if  not isinstance(value, StorePurchasedResp._data._attributes._purchases._billed_to):
                                    raise TypeError("billed_to must be StorePurchasedResp._data._attributes._purchases._billed_to")

                                self.__billed_to = value
                            billed_to = property(_get_billed_to, _set_billed_to)
                            
                            def _get_id(self):
                                return self.__id
                            def _set_id(self, value):
                                if  not isinstance(value, int):
                                    raise TypeError("id must be int")

                                self.__id = value
                            id = property(_get_id, _set_id)
                            
                            def _get_invoice_date(self):
                                return self.__invoice_date
                            def _set_invoice_date(self, value):
                                if  not isinstance(value, str):
                                    raise TypeError("invoice_date must be str")

                                self.__invoice_date = value
                            invoice_date = property(_get_invoice_date, _set_invoice_date)
                            
                            def _get_items(self):
                                return self.__items
                            def _set_items(self, value):
                                if  not isinstance(value, list):
                                    raise TypeError("items must be list")
                                if  not all(isinstance(i, StorePurchasedResp._data._attributes._purchases._items) for i in value):
                                    raise TypeError("items list values must be StorePurchasedResp._data._attributes._purchases._items")

                                self.__items = value
                            items = property(_get_items, _set_items)
                            
                            def _get_order_id(self):
                                return self.__order_id
                            def _set_order_id(self, value):
                                if  not isinstance(value, str):
                                    raise TypeError("order_id must be str")

                                self.__order_id = value
                            order_id = property(_get_order_id, _set_order_id)
                            
                            def _get_pending(self):
                                return self.__pending
                            def _set_pending(self, value):
                                if  not isinstance(value, bool):
                                    raise TypeError("pending must be bool")

                                self.__pending = value
                            pending = property(_get_pending, _set_pending)
                            
                            def _get_sub_total(self):
                                return self.__sub_total
                            def _set_sub_total(self, value):
                                if  not isinstance(value, str):
                                    raise TypeError("sub_total must be str")

                                self.__sub_total = value
                            sub_total = property(_get_sub_total, _set_sub_total)
                            
                            def _get_tax(self):
                                return self.__tax
                            def _set_tax(self, value):
                                if  not isinstance(value, str):
                                    raise TypeError("tax must be str")

                                self.__tax = value
                            tax = property(_get_tax, _set_tax)
                            
                            def _get_total(self):
                                return self.__total
                            def _set_total(self, value):
                                if  not isinstance(value, str):
                                    raise TypeError("total must be str")

                                self.__total = value
                            total = property(_get_total, _set_total)
                            
                            def _get_from_email_invoice(self):
                                return self.__from_email_invoice
                            def _set_from_email_invoice(self, value):
                                if  not isinstance(value, bool):
                                    raise TypeError("from_email_invoice must be bool")

                                self.__from_email_invoice = value
                            from_email_invoice = property(_get_from_email_invoice, _set_from_email_invoice)
                            
                            def _get_is_chargeback(self):
                                return self.__is_chargeback
                            def _set_is_chargeback(self, value):
                                if  not isinstance(value, bool):
                                    raise TypeError("is_chargeback must be bool")

                                self.__is_chargeback = value
                            is_chargeback = property(_get_is_chargeback, _set_is_chargeback)
                            
                            def _get_show_tax(self):
                                return self.__show_tax
                            def _set_show_tax(self, value):
                                if  not isinstance(value, bool):
                                    raise TypeError("show_tax must be bool")

                                self.__show_tax = value
                            show_tax = property(_get_show_tax, _set_show_tax)
                            
                            def _get_show_sub_total(self):
                                return self.__show_sub_total
                            def _set_show_sub_total(self, value):
                                if  not isinstance(value, bool):
                                    raise TypeError("show_sub_total must be bool")

                                self.__show_sub_total = value
                            show_sub_total = property(_get_show_sub_total, _set_show_sub_total)
                            
                            def _get_can_be_cleared_with_store_credit(self):
                                return self.__can_be_cleared_with_store_credit
                            def _set_can_be_cleared_with_store_credit(self, value):
                                if  not isinstance(value, bool):
                                    raise TypeError("can_be_cleared_with_store_credit must be bool")

                                self.__can_be_cleared_with_store_credit = value
                            can_be_cleared_with_store_credit = property(_get_can_be_cleared_with_store_credit, _set_can_be_cleared_with_store_credit)
                            
                            def _get_document_number(self):
                                return self.__document_number
                            def _set_document_number(self, value):
                                if value is not None and  not isinstance(value, str):
                                    raise TypeError("document_number must be str")

                                self.__document_number = value
                            document_number = property(_get_document_number, _set_document_number)
                            

                            @staticmethod
                            def from_dict(d):
                                v = {}
                                if "billed-to" in d:
                                    v["billed_to"] = StorePurchasedResp._data._attributes._purchases._billed_to.from_dict(d["billed-to"]) if hasattr(StorePurchasedResp._data._attributes._purchases._billed_to, 'from_dict') else d["billed-to"]
                                if "id" in d:
                                    v["id"] = int.from_dict(d["id"]) if hasattr(int, 'from_dict') else d["id"]
                                if "invoice-date" in d:
                                    v["invoice_date"] = str.from_dict(d["invoice-date"]) if hasattr(str, 'from_dict') else d["invoice-date"]
                                if "items" in d:
                                    v["items"] = [StorePurchasedResp._data._attributes._purchases._items.from_dict(p) if hasattr(StorePurchasedResp._data._attributes._purchases._items, 'from_dict') else p for p in d["items"]]
                                if "order-id" in d:
                                    v["order_id"] = str.from_dict(d["order-id"]) if hasattr(str, 'from_dict') else d["order-id"]
                                if "pending" in d:
                                    v["pending"] = bool.from_dict(d["pending"]) if hasattr(bool, 'from_dict') else d["pending"]
                                if "sub-total" in d:
                                    v["sub_total"] = str.from_dict(d["sub-total"]) if hasattr(str, 'from_dict') else d["sub-total"]
                                if "tax" in d:
                                    v["tax"] = str.from_dict(d["tax"]) if hasattr(str, 'from_dict') else d["tax"]
                                if "total" in d:
                                    v["total"] = str.from_dict(d["total"]) if hasattr(str, 'from_dict') else d["total"]
                                if "from-email-invoice" in d:
                                    v["from_email_invoice"] = bool.from_dict(d["from-email-invoice"]) if hasattr(bool, 'from_dict') else d["from-email-invoice"]
                                if "is-chargeback" in d:
                                    v["is_chargeback"] = bool.from_dict(d["is-chargeback"]) if hasattr(bool, 'from_dict') else d["is-chargeback"]
                                if "show-tax" in d:
                                    v["show_tax"] = bool.from_dict(d["show-tax"]) if hasattr(bool, 'from_dict') else d["show-tax"]
                                if "show-sub-total" in d:
                                    v["show_sub_total"] = bool.from_dict(d["show-sub-total"]) if hasattr(bool, 'from_dict') else d["show-sub-total"]
                                if "can-be-cleared-with-store-credit" in d:
                                    v["can_be_cleared_with_store_credit"] = bool.from_dict(d["can-be-cleared-with-store-credit"]) if hasattr(bool, 'from_dict') else d["can-be-cleared-with-store-credit"]
                                if "document-number" in d:
                                    v["document_number"] = str.from_dict(d["document-number"]) if hasattr(str, 'from_dict') else d["document-number"]
                                return StorePurchasedResp._data._attributes._purchases(**v)


                            def as_dict(self):
                                d = {}
                                if self.__billed_to is not None:
                                    d['billed-to'] = self.__billed_to.as_dict() if hasattr(self.__billed_to, 'as_dict') else self.__billed_to
                                if self.__id is not None:
                                    d['id'] = self.__id.as_dict() if hasattr(self.__id, 'as_dict') else self.__id
                                if self.__invoice_date is not None:
                                    d['invoice-date'] = self.__invoice_date.as_dict() if hasattr(self.__invoice_date, 'as_dict') else self.__invoice_date
                                if self.__items is not None:
                                    d['items'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__items]
                                if self.__order_id is not None:
                                    d['order-id'] = self.__order_id.as_dict() if hasattr(self.__order_id, 'as_dict') else self.__order_id
                                if self.__pending is not None:
                                    d['pending'] = self.__pending.as_dict() if hasattr(self.__pending, 'as_dict') else self.__pending
                                if self.__sub_total is not None:
                                    d['sub-total'] = self.__sub_total.as_dict() if hasattr(self.__sub_total, 'as_dict') else self.__sub_total
                                if self.__tax is not None:
                                    d['tax'] = self.__tax.as_dict() if hasattr(self.__tax, 'as_dict') else self.__tax
                                if self.__total is not None:
                                    d['total'] = self.__total.as_dict() if hasattr(self.__total, 'as_dict') else self.__total
                                if self.__from_email_invoice is not None:
                                    d['from-email-invoice'] = self.__from_email_invoice.as_dict() if hasattr(self.__from_email_invoice, 'as_dict') else self.__from_email_invoice
                                if self.__is_chargeback is not None:
                                    d['is-chargeback'] = self.__is_chargeback.as_dict() if hasattr(self.__is_chargeback, 'as_dict') else self.__is_chargeback
                                if self.__show_tax is not None:
                                    d['show-tax'] = self.__show_tax.as_dict() if hasattr(self.__show_tax, 'as_dict') else self.__show_tax
                                if self.__show_sub_total is not None:
                                    d['show-sub-total'] = self.__show_sub_total.as_dict() if hasattr(self.__show_sub_total, 'as_dict') else self.__show_sub_total
                                if self.__can_be_cleared_with_store_credit is not None:
                                    d['can-be-cleared-with-store-credit'] = self.__can_be_cleared_with_store_credit.as_dict() if hasattr(self.__can_be_cleared_with_store_credit, 'as_dict') else self.__can_be_cleared_with_store_credit
                                if self.__document_number is not None:
                                    d['document-number'] = self.__document_number.as_dict() if hasattr(self.__document_number, 'as_dict') else self.__document_number
                                return d

                            def __repr__(self):
                                return "<Class _purchases. billed_to: {}, id: {}, invoice_date: {}, items: {}, order_id: {}, pending: {}, sub_total: {}, tax: {}, total: {}, from_email_invoice: {}, is_chargeback: {}, show_tax: {}, show_sub_total: {}, can_be_cleared_with_store_credit: {}, document_number: {}>".format(limitedRepr(self.__billed_to[:20] if isinstance(self.__billed_to, bytes) else self.__billed_to), limitedRepr(self.__id[:20] if isinstance(self.__id, bytes) else self.__id), limitedRepr(self.__invoice_date[:20] if isinstance(self.__invoice_date, bytes) else self.__invoice_date), limitedRepr(self.__items[:20] if isinstance(self.__items, bytes) else self.__items), limitedRepr(self.__order_id[:20] if isinstance(self.__order_id, bytes) else self.__order_id), limitedRepr(self.__pending[:20] if isinstance(self.__pending, bytes) else self.__pending), limitedRepr(self.__sub_total[:20] if isinstance(self.__sub_total, bytes) else self.__sub_total), limitedRepr(self.__tax[:20] if isinstance(self.__tax, bytes) else self.__tax), limitedRepr(self.__total[:20] if isinstance(self.__total, bytes) else self.__total), limitedRepr(self.__from_email_invoice[:20] if isinstance(self.__from_email_invoice, bytes) else self.__from_email_invoice), limitedRepr(self.__is_chargeback[:20] if isinstance(self.__is_chargeback, bytes) else self.__is_chargeback), limitedRepr(self.__show_tax[:20] if isinstance(self.__show_tax, bytes) else self.__show_tax), limitedRepr(self.__show_sub_total[:20] if isinstance(self.__show_sub_total, bytes) else self.__show_sub_total), limitedRepr(self.__can_be_cleared_with_store_credit[:20] if isinstance(self.__can_be_cleared_with_store_credit, bytes) else self.__can_be_cleared_with_store_credit), limitedRepr(self.__document_number[:20] if isinstance(self.__document_number, bytes) else self.__document_number))




                    _types_map = {
                        'disabled_storefront': {'type': bool, 'subtype': None},
                        'purchases': {'type': list, 'subtype': _purchases},
                        'isActiveMediaLinkedAccount': {'type': bool, 'subtype': None},
                        'range': {'type': _range, 'subtype': None},
                        'storefront_id': {'type': int, 'subtype': None},
                        'is_complete': {'type': bool, 'subtype': None},
                        'can_pay_with_store_credit_enabled': {'type': bool, 'subtype': None},
                        'pagination_token': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'disabled_storefront': { 'required': True,},
                        'purchases': { 'required': True,},
                        'isActiveMediaLinkedAccount': { 'required': True,},
                        'range': { 'required': True,},
                        'storefront_id': { 'required': True,},
                        'is_complete': { 'required': True,},
                        'can_pay_with_store_credit_enabled': { 'required': True,},
                        'pagination_token': { 'required': True,},
                    }

                    def __init__(self
                            , disabled_storefront: bool=None            , purchases: List[_purchases]
                =None            , isActiveMediaLinkedAccount: bool=None            , range: _range=None            , storefront_id: int=None            , is_complete: bool=None            , can_pay_with_store_credit_enabled: bool=None            , pagination_token: str=None            ):
                        pass
                        self.__disabled_storefront = disabled_storefront
                        self.__purchases = purchases
                        self.__isActiveMediaLinkedAccount = isActiveMediaLinkedAccount
                        self.__range = range
                        self.__storefront_id = storefront_id
                        self.__is_complete = is_complete
                        self.__can_pay_with_store_credit_enabled = can_pay_with_store_credit_enabled
                        self.__pagination_token = pagination_token
                    
                    def _get_disabled_storefront(self):
                        return self.__disabled_storefront
                    def _set_disabled_storefront(self, value):
                        if  not isinstance(value, bool):
                            raise TypeError("disabled_storefront must be bool")

                        self.__disabled_storefront = value
                    disabled_storefront = property(_get_disabled_storefront, _set_disabled_storefront)
                    
                    def _get_purchases(self):
                        return self.__purchases
                    def _set_purchases(self, value):
                        if  not isinstance(value, list):
                            raise TypeError("purchases must be list")
                        if  not all(isinstance(i, StorePurchasedResp._data._attributes._purchases) for i in value):
                            raise TypeError("purchases list values must be StorePurchasedResp._data._attributes._purchases")

                        self.__purchases = value
                    purchases = property(_get_purchases, _set_purchases)
                    
                    def _get_isActiveMediaLinkedAccount(self):
                        return self.__isActiveMediaLinkedAccount
                    def _set_isActiveMediaLinkedAccount(self, value):
                        if  not isinstance(value, bool):
                            raise TypeError("isActiveMediaLinkedAccount must be bool")

                        self.__isActiveMediaLinkedAccount = value
                    isActiveMediaLinkedAccount = property(_get_isActiveMediaLinkedAccount, _set_isActiveMediaLinkedAccount)
                    
                    def _get_range(self):
                        return self.__range
                    def _set_range(self, value):
                        if  not isinstance(value, StorePurchasedResp._data._attributes._range):
                            raise TypeError("range must be StorePurchasedResp._data._attributes._range")

                        self.__range = value
                    range = property(_get_range, _set_range)
                    
                    def _get_storefront_id(self):
                        return self.__storefront_id
                    def _set_storefront_id(self, value):
                        if  not isinstance(value, int):
                            raise TypeError("storefront_id must be int")

                        self.__storefront_id = value
                    storefront_id = property(_get_storefront_id, _set_storefront_id)
                    
                    def _get_is_complete(self):
                        return self.__is_complete
                    def _set_is_complete(self, value):
                        if  not isinstance(value, bool):
                            raise TypeError("is_complete must be bool")

                        self.__is_complete = value
                    is_complete = property(_get_is_complete, _set_is_complete)
                    
                    def _get_can_pay_with_store_credit_enabled(self):
                        return self.__can_pay_with_store_credit_enabled
                    def _set_can_pay_with_store_credit_enabled(self, value):
                        if  not isinstance(value, bool):
                            raise TypeError("can_pay_with_store_credit_enabled must be bool")

                        self.__can_pay_with_store_credit_enabled = value
                    can_pay_with_store_credit_enabled = property(_get_can_pay_with_store_credit_enabled, _set_can_pay_with_store_credit_enabled)
                    
                    def _get_pagination_token(self):
                        return self.__pagination_token
                    def _set_pagination_token(self, value):
                        if  not isinstance(value, str):
                            raise TypeError("pagination_token must be str")

                        self.__pagination_token = value
                    pagination_token = property(_get_pagination_token, _set_pagination_token)
                    

                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "disabled-storefront" in d:
                            v["disabled_storefront"] = bool.from_dict(d["disabled-storefront"]) if hasattr(bool, 'from_dict') else d["disabled-storefront"]
                        if "purchases" in d:
                            v["purchases"] = [StorePurchasedResp._data._attributes._purchases.from_dict(p) if hasattr(StorePurchasedResp._data._attributes._purchases, 'from_dict') else p for p in d["purchases"]]
                        if "isActiveMediaLinkedAccount" in d:
                            v["isActiveMediaLinkedAccount"] = bool.from_dict(d["isActiveMediaLinkedAccount"]) if hasattr(bool, 'from_dict') else d["isActiveMediaLinkedAccount"]
                        if "range" in d:
                            v["range"] = StorePurchasedResp._data._attributes._range.from_dict(d["range"]) if hasattr(StorePurchasedResp._data._attributes._range, 'from_dict') else d["range"]
                        if "storefront-id" in d:
                            v["storefront_id"] = int.from_dict(d["storefront-id"]) if hasattr(int, 'from_dict') else d["storefront-id"]
                        if "is-complete" in d:
                            v["is_complete"] = bool.from_dict(d["is-complete"]) if hasattr(bool, 'from_dict') else d["is-complete"]
                        if "can-pay-with-store-credit-enabled" in d:
                            v["can_pay_with_store_credit_enabled"] = bool.from_dict(d["can-pay-with-store-credit-enabled"]) if hasattr(bool, 'from_dict') else d["can-pay-with-store-credit-enabled"]
                        if "pagination-token" in d:
                            v["pagination_token"] = str.from_dict(d["pagination-token"]) if hasattr(str, 'from_dict') else d["pagination-token"]
                        return StorePurchasedResp._data._attributes(**v)


                    def as_dict(self):
                        d = {}
                        if self.__disabled_storefront is not None:
                            d['disabled-storefront'] = self.__disabled_storefront.as_dict() if hasattr(self.__disabled_storefront, 'as_dict') else self.__disabled_storefront
                        if self.__purchases is not None:
                            d['purchases'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__purchases]
                        if self.__isActiveMediaLinkedAccount is not None:
                            d['isActiveMediaLinkedAccount'] = self.__isActiveMediaLinkedAccount.as_dict() if hasattr(self.__isActiveMediaLinkedAccount, 'as_dict') else self.__isActiveMediaLinkedAccount
                        if self.__range is not None:
                            d['range'] = self.__range.as_dict() if hasattr(self.__range, 'as_dict') else self.__range
                        if self.__storefront_id is not None:
                            d['storefront-id'] = self.__storefront_id.as_dict() if hasattr(self.__storefront_id, 'as_dict') else self.__storefront_id
                        if self.__is_complete is not None:
                            d['is-complete'] = self.__is_complete.as_dict() if hasattr(self.__is_complete, 'as_dict') else self.__is_complete
                        if self.__can_pay_with_store_credit_enabled is not None:
                            d['can-pay-with-store-credit-enabled'] = self.__can_pay_with_store_credit_enabled.as_dict() if hasattr(self.__can_pay_with_store_credit_enabled, 'as_dict') else self.__can_pay_with_store_credit_enabled
                        if self.__pagination_token is not None:
                            d['pagination-token'] = self.__pagination_token.as_dict() if hasattr(self.__pagination_token, 'as_dict') else self.__pagination_token
                        return d

                    def __repr__(self):
                        return "<Class _attributes. disabled_storefront: {}, purchases: {}, isActiveMediaLinkedAccount: {}, range: {}, storefront_id: {}, is_complete: {}, can_pay_with_store_credit_enabled: {}, pagination_token: {}>".format(limitedRepr(self.__disabled_storefront[:20] if isinstance(self.__disabled_storefront, bytes) else self.__disabled_storefront), limitedRepr(self.__purchases[:20] if isinstance(self.__purchases, bytes) else self.__purchases), limitedRepr(self.__isActiveMediaLinkedAccount[:20] if isinstance(self.__isActiveMediaLinkedAccount, bytes) else self.__isActiveMediaLinkedAccount), limitedRepr(self.__range[:20] if isinstance(self.__range, bytes) else self.__range), limitedRepr(self.__storefront_id[:20] if isinstance(self.__storefront_id, bytes) else self.__storefront_id), limitedRepr(self.__is_complete[:20] if isinstance(self.__is_complete, bytes) else self.__is_complete), limitedRepr(self.__can_pay_with_store_credit_enabled[:20] if isinstance(self.__can_pay_with_store_credit_enabled, bytes) else self.__can_pay_with_store_credit_enabled), limitedRepr(self.__pagination_token[:20] if isinstance(self.__pagination_token, bytes) else self.__pagination_token))




            _types_map = {
                'id': {'type': str, 'subtype': None},
                'type': {'type': str, 'subtype': None},
                'attributes': {'type': _attributes, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'id': { 'required': True,},
                'type': { 'required': True,},
                'attributes': { 'required': True,},
            }

            def __init__(self
                    , id: str=None            , type: str=None            , attributes: _attributes=None            ):
                pass
                self.__id = id
                self.__type = type
                self.__attributes = attributes
            
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
            
            def _get_attributes(self):
                return self.__attributes
            def _set_attributes(self, value):
                if  not isinstance(value, StorePurchasedResp._data._attributes):
                    raise TypeError("attributes must be StorePurchasedResp._data._attributes")

                self.__attributes = value
            attributes = property(_get_attributes, _set_attributes)
            

            @staticmethod
            def from_dict(d):
                v = {}
                if "id" in d:
                    v["id"] = str.from_dict(d["id"]) if hasattr(str, 'from_dict') else d["id"]
                if "type" in d:
                    v["type"] = str.from_dict(d["type"]) if hasattr(str, 'from_dict') else d["type"]
                if "attributes" in d:
                    v["attributes"] = StorePurchasedResp._data._attributes.from_dict(d["attributes"]) if hasattr(StorePurchasedResp._data._attributes, 'from_dict') else d["attributes"]
                return StorePurchasedResp._data(**v)


            def as_dict(self):
                d = {}
                if self.__id is not None:
                    d['id'] = self.__id.as_dict() if hasattr(self.__id, 'as_dict') else self.__id
                if self.__type is not None:
                    d['type'] = self.__type.as_dict() if hasattr(self.__type, 'as_dict') else self.__type
                if self.__attributes is not None:
                    d['attributes'] = self.__attributes.as_dict() if hasattr(self.__attributes, 'as_dict') else self.__attributes
                return d

            def __repr__(self):
                return "<Class _data. id: {}, type: {}, attributes: {}>".format(limitedRepr(self.__id[:20] if isinstance(self.__id, bytes) else self.__id), limitedRepr(self.__type[:20] if isinstance(self.__type, bytes) else self.__type), limitedRepr(self.__attributes[:20] if isinstance(self.__attributes, bytes) else self.__attributes))




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
        if  not isinstance(value, StorePurchasedResp._data):
            raise TypeError("data must be StorePurchasedResp._data")

        self.__data = value
    data = property(_get_data, _set_data)
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "data" in d:
            v["data"] = StorePurchasedResp._data.from_dict(d["data"]) if hasattr(StorePurchasedResp._data, 'from_dict') else d["data"]
        return StorePurchasedResp(**v)


    def as_dict(self):
        d = {}
        if self.__data is not None:
            d['data'] = self.__data.as_dict() if hasattr(self.__data, 'as_dict') else self.__data
        return d

    def __repr__(self):
        return "<Class StorePurchasedResp. data: {}>".format(limitedRepr(self.__data[:20] if isinstance(self.__data, bytes) else self.__data))

