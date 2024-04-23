import json
from enum import Enum

import requests
from config import CLIENT_ID, API_KEY

url = "https://api-seller.ozon.ru/v2/posting/fbo/list"
url2 = "https://api-seller.ozon.ru/v3/posting/fbs/get"

asd = {
  "dir": "ASC",
  "filter": {
    "since": "2024-04-01T00:00:00.000Z",
    "status": "delivered",
    "to": "2024-04-01T23:59:59.828Z"
  },
  "limit": 1000,
  "offset": 0,
  "translit": True,
  "with": {
    "analytics_data": True,
    "financial_data": True
  }
}

ert = {
  "posting_number": "0153222618-0004-1",
  "with": {
    "analytics_data": False,
    "barcodes": False,
    "financial_data": True,
    "product_exemplars": False,
    "translit": True
  }
}


response = requests.post(url=url, headers={'Client-Id': CLIENT_ID, 'Api-Key': API_KEY}, json=asd)
response2 = requests.post(url=url2, headers={'Client-Id': "129047", 'Api-Key': "06ef9d66-b383-4498-b75d-b5df7df4ce19"}, json=ert)

print(response2.text)


class OperationTypeEnum(str, Enum):
    empty = ''
    client_return_agent_operation = 'ClientReturnAgentOperation'
    marketplace_marketing_action_cost_operation = 'MarketplaceMarketingActionCostOperation'
    marketplace_sale_reviews_operation = 'MarketplaceSaleReviewsOperation'
    MarketplaceSellerCompensationOperation = 'MarketplaceSellerCompensationOperation'
    OperationAgentDeliveredToCustomer = 'OperationAgentDeliveredToCustomer'
    OperationAgentDeliveredToCustomerCanceled = 'OperationAgentDeliveredToCustomerCanceled'
    OperationAgentStornoDeliveredToCustomer = 'OperationAgentStornoDeliveredToCustomer'
    OperationClaim = 'OperationClaim'
    OperationCorrectionSeller = 'OperationCorrectionSeller'
    OperationDefectiveWriteOff = 'OperationDefectiveWriteOff'
    OperationLackWriteOff = 'OperationLackWriteOff'
    OperationItemReturn = 'OperationItemReturn'
    OperationMarketplaceCrossDockServiceWriteOff = 'OperationMarketplaceCrossDockServiceWriteOff'
    OperationMarketplaceServiceStorage = 'OperationMarketplaceServiceStorage'
    OperationSetOff = 'OperationSetOff'
    MarketplaceSellerReexposureDeliveryReturnOperation = 'MarketplaceSellerReexposureDeliveryReturnOperation'
    OperationReturnGoodsFBSofRMS = 'OperationReturnGoodsFBSofRMS'
    ReturnAgentOperationRFBS = 'ReturnAgentOperationRFBS'
    MarketplaceSellerShippingCompensationReturnOperation = 'MarketplaceSellerShippingCompensationReturnOperation'
    OperationMarketplaceServicePremiumCashback = 'OperationMarketplaceServicePremiumCashback'
    MarketplaceServicePremiumPromotion = 'MarketplaceServicePremiumPromotion'
    MarketplaceRedistributionOfAcquiringOperation = 'MarketplaceRedistributionOfAcquiringOperation'
    MarketplaceReturnStorageServiceAtThePickupPointFbsItem = 'MarketplaceReturnStorageServiceAtThePickupPointFbsItem'
    MarketplaceReturnStorageServiceInTheWarehouseFbsItem = 'MarketplaceReturnStorageServiceInTheWarehouseFbsItem'
    MarketplaceServiceItemDeliveryKGT = 'MarketplaceServiceItemDeliveryKGT'
    MarketplaceServiceItemDirectFlowLogistic = 'MarketplaceServiceItemDirectFlowLogistic'
    MarketplaceServiceItemReturnFlowLogistic = 'MarketplaceServiceItemReturnFlowLogistic'
    MarketplaceServicePremiumCashbackIndividualPoints = 'MarketplaceServicePremiumCashbackIndividualPoints'
    OperationMarketplaceWithHoldingForUndeliverableGoods = 'OperationMarketplaceWithHoldingForUndeliverableGoods'
    MarketplaceServiceItemDirectFlowLogisticVDC = 'MarketplaceServiceItemDirectFlowLogisticVDC'
    MarketplaceServiceItemDropoffPPZ = 'MarketplaceServiceItemDropoffPPZ'
    MarketplaceServicePremiumCashback = 'MarketplaceServicePremiumCashback'
    MarketplaceServiceItemRedistributionReturnsPVZ = 'MarketplaceServiceItemRedistributionReturnsPVZ'

for f in OperationTypeEnum:
    t = [s for s in f.strip()]
    for i, c in enumerate(t):
        if c.isupper():
            if i == 0:
                t[i] = c.lower()
            else:
                t[i] = f'_{c.lower()}'
    print(''.join(t))