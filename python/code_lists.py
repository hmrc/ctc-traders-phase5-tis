"""
 Copyright 2023 HM Revenue & Customs

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
# Codelist to URLs
code_lists: dict[str, str] = {
    "CL008": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip",
    "CL009": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip",
    "CL010": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip",
    "CL016": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CUSCode.zip",
    "CL017": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackages.zip",
    "CL019": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_IncidentCode.zip",
    "CL027": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip",
    "CL038": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_QualifierOfIdentificationIncident.zip",
    "CL042": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeAdditional.zip",
    "CL048": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CurrencyCodes.zip",
    "CL060": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_MessageTypes.zip",
    "CL070": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCustomsOfficeLists.zip",
    "CL076": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeWithReference.zip",
    "CL094": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_RepresentativeStatusCode.zip",
    "CL101": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnDangerousGoodsCode.zip",
    "CL112": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip",
    "CL116": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportChargesMethodOfPayment.zip",
    "CL141": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/COL-Generic-20230601.zip",
    "CL147": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCustomsSecurityAgreementArea.zip",
    "CL152": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_HScode.zip",
    "CL163": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_ReleaseType.zip",
    "CL164": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_ReleaseNotification.zip",
    "CL165": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip",
    "CL171": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDeparture.zip",
    "CL172": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDestination.zip",
    "CL173": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeTransit.zip",
    "CL175": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeTransitExit.zip",
    "CL177": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeRecovery.zip",
    "CL178": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentUnionGoods.zip",
    "CL180": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_FunctionalErrorCodesIeCA.zip",
    "CL181": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackagesBulk.zip",
    "CL182": "../downloads/CL182.zip",
    "CL190": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryAddressPostcodeBased.zip",
    "CL192": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_LanguageByCustoms.zip",
    "CL195": "../downloads/CL195.zip",
    "CL198": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryAddressPostcodeOnly.zip",
    "CL211": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_NoReleaseMotivation.zip",
    "CL213": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip",
    "CL214": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentType.zip",
    "CL215": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_RequestedDocumentType.zip",
    "CL217": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeSecurity.zip",
    "CL218": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportModeCode.zip",
    "CL219": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationofMeansOfTransportActive.zip",
    "CL226": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_RejectionCodeDepartureExport.zip",
    "CL227": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_RejectionCodeDepartureExport.zip",
    "CL229": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeCTC.zip",
    "CL230": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeEUNonTIR.zip",
    "CL231": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationType.zip",
    "CL232": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeItemLevel.zip",
    "CL234": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip",
    "CL235": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AuthorisationTypeDeparture.zip",
    "CL236": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AuthorisationTypeDestination.zip",
    "CL239": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalInformation.zip",
    "CL244": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnLocodeExtended.zip",
    "CL248": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip",
    "CL251": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeType.zip",
    "CL252": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_InvalidGuaranteeReason.zip",
    "CL286": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeWithGRN.zip",
    "CL294": "../downloads/CL294.zip",
    "CL296": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SpecificCircumstanceIndicatorCode.zip",
    "CL326": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_QualifierOfTheIdentification.zip",
    "CL347": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfLocation.zip",
    "CL349": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Unit.zip",
    "CL380": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip",
    "CL384": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_NotificationType.zip",
    "CL385": "../downloads/CL385.zip",
    "CL505": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryWithoutZip.zip",
    "CL553": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_MSCountry.zip",
    "CL560": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_BusinessRejectionTypeDepExp.zip",
    "CL570": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_BusinessRejectionTypeDesExt.zip",
    "CL610": "../downloads/CL610.zip",
    "CL704": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalSupplyChainActorRoleCode.zip",
    "CL716": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_ControlType.zip",
    "CL750": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip",
    "CL754": "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip"
}


def replace_code_list(cl: str) -> str:
    """
    If the codelist exists in the dict, wraps the codelist in an HTML link. Else, returns the codelist
    :param cl: The codelist
    :return: The codelist, with or without a hyperlink wrapping
    """
    if code_lists.__contains__(cl):
        return f"""<a href="{code_lists.get(cl)}">{cl}</a>"""
    else:
        return cl


def replace_code_list_full_string(string: str) -> str:
    """
    Takes a string and adds links to any known codelists

    :param string: The string
    :return: The linkified string
    """
    replaced = string
    for key, item in code_lists.items():
        replaced = replaced.replace(key, replace_code_list(key))
    return replaced
