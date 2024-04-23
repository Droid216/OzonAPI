from .base import BaseRequest
from pydantic import Field
from enum import Enum
from rfc3339_validator import validate_rfc3339
from pydantic import validator


class FinanceTransactionListDate(BaseRequest):
    from_field: str = Field(serialization_alias='from')
    to: str

    @validator('from_field')
    def validate_from_field(cls, v):
        if not validate_rfc3339(v):
            raise ValueError("date_start must be rfc3339 valid")
        return v

    @validator('to')
    def validate_to(cls, v):
        if not validate_rfc3339(v):
            raise ValueError("date_start must be rfc3339 valid")
        return v


class OperationTypeEnum(str, Enum):
    empty = ''
    client_return_agent_operation = 'ClientReturnAgentOperation'
    marketplace_marketing_action_cost_operation = 'MarketplaceMarketingActionCostOperation'
    marketplace_sale_reviews_operation = 'MarketplaceSaleReviewsOperation'
    marketplace_seller_compensation_operation = 'MarketplaceSellerCompensationOperation'
    operation_agent_delivered_to_customer = 'OperationAgentDeliveredToCustomer'
    operation_agent_delivered_to_customer_canceled = 'OperationAgentDeliveredToCustomerCanceled'
    operation_agent_storno_delivered_to_customer = 'OperationAgentStornoDeliveredToCustomer'
    operation_claim = 'OperationClaim'
    operation_correction_seller = 'OperationCorrectionSeller'
    operation_defective_write_off = 'OperationDefectiveWriteOff'
    operation_lack_write_off = 'OperationLackWriteOff'
    operation_item_return = 'OperationItemReturn'
    operation_marketplace_cross_dock_service_write_off = 'OperationMarketplaceCrossDockServiceWriteOff'
    operation_marketplace_service_storage = 'OperationMarketplaceServiceStorage'
    operation_set_off = 'OperationSetOff'
    marketplace_seller_reexposure_delivery_return_operation = 'MarketplaceSellerReexposureDeliveryReturnOperation'
    operation_return_goods_fbs_of_rms = 'OperationReturnGoodsFBSofRMS'
    return_agent_operation_rfbs = 'ReturnAgentOperationRFBS'
    marketplace_seller_shipping_compensation_return_operation = 'MarketplaceSellerShippingCompensationReturnOperation'
    operation_marketplace_service_premium_cashback = 'OperationMarketplaceServicePremiumCashback'
    marketplace_service_premium_promotion = 'MarketplaceServicePremiumPromotion'
    marketplace_redistribution_of_acquiring_operation = 'MarketplaceRedistributionOfAcquiringOperation'
    marketplace_return_storage_service_at_the_pickup_point_fbs_item = 'MarketplaceReturnStorageServiceAtThePickupPointFbsItem'
    marketplace_return_storage_service_in_the_warehouse_fbs_item = 'MarketplaceReturnStorageServiceInTheWarehouseFbsItem'
    marketplace_service_item_delivery_kgt = 'MarketplaceServiceItemDeliveryKGT'
    marketplace_service_item_direct_flow_logistic = 'MarketplaceServiceItemDirectFlowLogistic'
    marketplace_service_item_return_flow_logistic = 'MarketplaceServiceItemReturnFlowLogistic'
    marketplace_service_premium_cashback_individual_points = 'MarketplaceServicePremiumCashbackIndividualPoints'
    operation_marketplace_with_holding_for_undeliverable_goods = 'OperationMarketplaceWithHoldingForUndeliverableGoods'
    marketplace_service_item_direct_flow_logistic_vdc = 'MarketplaceServiceItemDirectFlowLogisticVDC'
    marketplace_service_item_drop_off_ppz = 'MarketplaceServiceItemDropoffPPZ'
    marketplace_service_premium_cashback = 'MarketplaceServicePremiumCashback'
    marketplace_service_item_redistribution_returns_pvz = 'MarketplaceServiceItemRedistributionReturnsPVZ'


class TransactionTypeEnum(str, Enum):
    all = 'all'
    services = 'services'
    compensation = 'compensation'
    transfer_delivery = 'transferDelivery'
    other = 'other'


class FinanceTransactionListFilter(BaseRequest):
    date: FinanceTransactionListDate
    operation_type: list[str]
    posting_number: str
    transaction_type: str


class FinanceTransactionListRequest(BaseRequest):
    filter: FinanceTransactionListFilter
    page: int
    page_size: int
