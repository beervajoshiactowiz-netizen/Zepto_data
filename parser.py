from parsel import Selector
import json
from pprint import pprint
def parser(raw_data: dict):

    selector = Selector(json.dumps(raw_data), type='json')
    result = []

    for item in selector.jmespath('layout'):

        for items in item.jmespath('data.resolver.data.items'):
            items_data = {}
            items_data["brand"]=items.jmespath('productResponse.product.brand').get()
            items_data["brand_id"]=items.jmespath('productResponse.product.brandId').get()
            items_data["country_origin"] = items.jmespath('productResponse.product.countryOfOrigin').get()
            items_data["description"] = [items.jmespath('productResponse.product.description').get()]
            items_data["ingredients"] = items.jmespath('productResponse.product.ingredients').get()
            items_data["manufacturerName"]=items.jmespath('productResponse.product.manufacturerName').get()
            items_data["item_name"] = items.jmespath('productResponse.product.name').get()
            items_data["variant_id"] = items.jmespath('productResponse.productVariant.id').get()
            items_data["item_pack_size"] = items.jmespath('productResponse.productVariant.formattedPacksize').get()
            for i in items.jmespath('productResponse.productVariant.images'):

                items_data["item_image"] = i.jmespath('path').get()
            items_data["item_max_quantity"] = items.jmespath('productResponse.productVariant.maxAllowedQuantity').get()
            items_data["item_mrp"] = items.jmespath('productResponse.productVariant.mrp').get()
            items_data["item_packsize"] = items.jmespath('productResponse.productVariant.packsize').get()
            items_data["item_shelflifeinHour"] = items.jmespath('productResponse.productVariant.shelfLifeInHours').get()
            items_data["unitOfMeasure"] = items.jmespath('productResponse.productVariant.unitOfMeasure').get()
            items_data["item_id"] = items.jmespath('productResponse.productVariant.productId').get()
            items_data["rating"] = items.jmespath('productResponse.productVariant.ratingSummary').get()
            items_data["item_type"] = items.jmespath('productResponse.productType').get()
            items_data["discounted_sellingprice"] = items.jmespath('productResponse.discountedSellingPrice').get()
            items_data["discount_amount"] = items.jmespath('productResponse.discountAmount').get()
            items_data["category"] = items.jmespath('productResponse.primaryCategoryName').get()

            result.append(items_data)
    pprint(result)
    return result