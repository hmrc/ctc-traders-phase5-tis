## R0003

**Functional Description**

Each &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED). Reference number&gt; is unique throughout the
declaration.

**Technical Description**

Each /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber is unique throughout the declaration.


## R0004

**Functional Description**

The value of &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt; field
is considered valid only if it is not LESS than or EQUAL to &lt;TRANSIT OPERATION.Release date&gt;

**Technical Description**

The value of /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/arrivalDateAndTimeEstimated field is considered valid<br />
only if it is not LESS than or EQUAL to /<span>&#42;</span>/TransitOperation/releaseDate


## R0005

**Functional Description**

The value of &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED).Arrival date and time estimated&gt; field
is considered valid only if it is not LESS than or EQUAL to &lt;MESSAGE. Preparation date and time&gt;

**Technical Description**

The value of /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/arrivalDateAndTimeEstimated field is considered valid<br />
only if it is not LESS than or EQUAL to /<span>&#42;</span>/Message/Preparation date and time


## R0006

**Functional Description**

IF the first two characters of &lt;CUSTOMS OFFICE OF DESTINATION (DECLARED). Reference
number&gt; is in set <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> (CountryCodesCTC)
THEN the first two characters of at least one instance of &lt;CUSTOMS OFFICE OF TRANSIT
(DECLARED). Reference number&gt; shall be EQUAL to the first two characters of &lt;CUSTOMS OFFICE
OF DESTINATION (DECLARED). Reference number&gt;;
IF the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt; is in set
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> (CountryCodesCTC) AND If the first two characters of &lt;CUSTOMS OFFICE OF DESTINATION
(DECLARED). Reference number&gt; is in set <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity)
THEN the first two characters of at least one instance of &lt;CUSTOMS OFFICE OF TRANSIT
(DECLARED). Reference number&gt; shall be in set <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity).

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in set <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a><br />
THEN the first two characters of at least one instance of<br />
/<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber shall be EQUAL to the first two characters of<br />
/<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber;<br />
If the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in set <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> AND If the<br />
first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in set <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
THEN the first two characters of at least one instance of<br />
/<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber shall be in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a>.


## R0007

**Functional Description**

Each &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration goods item
number&gt; is unique throughout the declaration. The items shall be numbered in a sequential fashion,
starting from '1' for the first item and increment the numbering by '1' for each following item.

**Technical Description**

Each /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationGoodsItemNumber is unique<br />
throughout the declaration. The items shall be numbered in a sequential fashion, starting from '1' for<br />
the first item and increment the numbering by '1' for each following item.


## R0008

**Functional Description**

&lt;Correlation identifier&gt; shall be EQUAL to the &lt;Message identification&gt; of the request/rejected
message.

**Technical Description**

/<span>&#42;</span>/correlationIdentifier shall be EQUAL to the /<span>&#42;</span>/messageIdentification of the request/rejected message.


## R0020

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F} AND the first two characters of
&lt;CUSTOMS OFFICE OF DEPARTURE.Reference number&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> (CountryCodesCTC)
THEN
(at least one &lt;CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentUnionGoods.zip">CL178</a>
(PreviousDocumentUnionGoods)) OR
(at least one &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS
DOCUMENT.Type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentUnionGoods.zip">CL178</a> (PreviousDocumentUnionGoods))
for each and every Consignment Item
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is in SET
{T2, T2F}
AND the first two characters of &lt;CUSTOMS OFFICE OF DEPARTURE.Reference
number&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> (CountryCodesCTC)
THEN
(at least one &lt;CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentUnionGoods.zip">CL178</a>
(PreviousDocumentUnionGoods)) OR
(at least one &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS
DOCUMENT.Type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentUnionGoods.zip">CL178</a> (PreviousDocumentUnionGoods)
for this ‘Consignment item’)

**Technical Description**

IF /<span>&#42;</span>/Transit Operation/declarationType is in SET {T2, T2F}<br />
AND the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a><br />
THEN<br />
(at least one /<span>&#42;</span>/Consignment/PreviousDocument/type is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentUnionGoods.zip">CL178</a>) OR<br />
(at least one /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/type is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentUnionGoods.zip">CL178</a>) for each and every Consignment Item<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2, T2F}<br />
AND the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a><br />
THEN<br />
(at least one /<span>&#42;</span>/Consignment/PreviousDocument/type is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentUnionGoods.zip">CL178</a>) OR<br />
(at least one /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/PreviousDocument/type is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentUnionGoods.zip">CL178</a> for this ‘Consignment item’)


## R0023

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL
REFERENCE.Type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a> (DocumentTypeExcise)
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL
REFERENCE.Reference number&gt; shall not be ‘0’ (zero)

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/type is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a><br />
(DocumentTypeExcise)<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/referenceNumber<br />
shall not be ‘0’ (zero)


## R0028

**Functional Description**

The structure of this Data Item is validated as specified in DDCOM. The check digit must follow the
ISO 6346 standard.

**Technical Description**

The structure of this Data Item is validated as specified in DDCOM. The check digit must follow the<br />
ISO 6346 standard.


## R0054

**Functional Description**

Numbering of items:
IF a discrepancy is identified in the Data Group THEN:
  - 'Sequence number' shall be unique AND EQUAL to the sequence number of the Data
 Group defined in the declaration for which the discrepancy is reported.<br /><br />
IF a new Data Group is identified THEN:
   - 'Sequence number' shall be unique AND EQUAL to the number of the last sequence
 number of the Data Group
  + 1 and the rest of the Data Items contained in the Data Group and all sub–Data Groups
  shall be filled in except for the Data Elements that are defined as optional or dependent
  in the declaration.<br /><br />
IF the information related to a Data Group is missing
THEN:
   - 'Sequence number' shall be unique AND EQUAL to the sequence number of the Data
  Group defined in the declaration
  and the rest of the Data Items contained in the Data Group and all sub–Data Groups
  shall not be filled.<br /><br />
Note: The Sequence number of a Data Group is unique if the XPath and the value of the sequence
number of this Data Item is unique in this message.

**Technical Description**

Numbering of items:<br />
IF a discrepancy is identified in the Data Group THEN:<br />
  - 'Sequence number' shall be unique AND EQUAL to the sequence number of the Data<br />
 Group defined in the declaration for which the discrepancy is reported.<br />
IF a new Data Group is identified THEN:<br />
   - 'Sequence number' shall be unique AND EQUAL to the number of the last sequence<br />
 number of the Data Group<br />
  + 1 and the rest of the Data Items contained in the Data Group and all sub–Data Groups<br />
  shall be filled in except for the Data Elements that are defined as optional or dependent<br />
  in the declaration.<br />
IF the information related to a Data Group is missing<br />
THEN:<br />
   - 'Sequence number' shall be unique AND EQUAL to the sequence number of the Data<br />
  Group defined in the declaration<br />
  and the rest of the Data Items contained in the Data Group and all sub–Data Groups<br />
  shall not be filled.<br />
Note: The Sequence number of a Data Group is unique if the XPath and the value of the sequence<br />
number of this Data Item is unique in this message.


## R0055

**Functional Description**

Numbering of items:
IF a discrepancy is identified in the Data Group THEN:
  - ‘Declaration goods item number' shall be unique AND EQUAL to the declaration goods item
 number defined in the declaration for which the discrepancy is reported AND
  - 'Goods item number’ shall be unique AND EQUAL to the goods item number defined in the
declaration for which the discrepancy is reported.<br /><br />
IF a new Data Group is identified THEN:
   - ‘Declaration goods item number' shall be unique AND EQUAL to the last declaration goods item
  number defined in the declaration + 1 AND
   - 'Goods item number’ shall be unique AND EQUAL to the last goods item number defined in the
  declaration + 1 AND
  the rest of the Data Items contained in the Data Group and all sub–Data Groups shall be
  filled in except for the Data Elements that are defined as optional or dependent in the
  declaration.<br /><br />
IF a Goods item is missing THEN:
   - ‘Declaration goods item number' shall be unique AND EQUAL to the number of the declaration
  goods item number defined in the declaration AND
   - 'Goods item number’ shall be unique AND EQUAL to the item number defined in the
  declaration AND the rest of the Data Items contained in the Data Group and all sub–Data Groups
  shall not be filled.<br /><br />
Note: The Sequence number of a Data Group is unique if the XPath and the value of the sequence
number of this Data Item is unique in this message.

**Technical Description**

Numbering of items:<br />
IF a discrepancy is identified in the Data Group THEN:<br />
  - ‘Declaration goods item number' shall be unique AND EQUAL to the declaration goods item<br />
 number defined in the declaration for which the discrepancy is reported AND<br />
  - 'Goods item number’ shall be unique AND EQUAL to the goods item number defined in the<br />
declaration for which the discrepancy is reported.<br />
IF a new Data Group is identified THEN:<br />
   - ‘Declaration goods item number' shall be unique AND EQUAL to the last declaration goods item<br />
  number defined in the declaration + 1 AND<br />
   - 'Goods item number’ shall be unique AND EQUAL to the last goods item number defined in the<br />
  declaration + 1 AND<br />
  the rest of the Data Items contained in the Data Group and all sub–Data Groups shall be<br />
  filled in except for the Data Elements that are defined as optional or dependent in the<br />
  declaration.<br />
IF a Goods item is missing THEN:<br />
   - ‘Declaration goods item number' shall be unique AND EQUAL to the number of the declaration<br />
  goods item number defined in the declaration AND<br />
   - 'Goods item number’ shall be unique AND EQUAL to the item number defined in the<br />
  declaration AND the rest of the Data Items contained in the Data Group and all sub–Data Groups<br />
  shall not be filled.<br />
Note: The Sequence number of a Data Group is unique if the XPath and the value of the sequence<br />
number of this Data Item is unique in this message.


## R0060

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-COMMODITY
CODE.Combined nomenclature code&gt; is PRESENT
THEN the concatenation of the Data Items &lt;CONSIGNMENT-HOUSE CONSIGNMENT-
CONSIGNMENT ITEM-COMMODITY-COMMODITY CODE.Harmonized System sub-heading code&gt;
(an6) and &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-
COMMODITY CODE.Combined nomenclature code&gt; (an2) must be a valid code in the TARIC
database (validated only by the EU countries).

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/<br />
CommodityCode/combinedNomenclatureCode is PRESENT<br />
THEN the concatenation of the Data Items /<span>&#42;</span>/Consignment/HouseConsignment/<br />
ConsignmentItem/Commodity/CommodityCode/harmonizedSystemSubHeadingCode (an6) and<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/<br />
CommodityCode/combinedNomenclatureCode (an2) must be a valid code in the TARIC database<br />
(validated only by the EU countries).


## R0076

**Functional Description**

IF &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS.Type of identification&gt; is in SET
{10,21,30,40,41,80}
THEN &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS. Identification number&gt; must not
contain lowercase letters.

**Technical Description**

IF /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/typeOfIdentification is in SET {10,21,30,40,41,80}<br />
THEN /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans/identificationNumber shall not contain lowercase<br />
letters.


## R0100

**Functional Description**

If &lt;TRADER AT DESTINATION.Communication language at destination&gt; is PRESENT, then the
indicated language is used as the basic language in any further communication between the Trader
and the Customs system. If &lt;TRADER AT DESTINATION.Communication language at destination&gt; is
not PRESENT then the Customs system will use the default language of the Office concerned;
If &lt;TRANSIT OPERATION.Communication language at departure&gt; is PRESENT, then the indicated
language is used as the basic language in any further communication between the Trader and the
Customs system. If &lt;TRANSIT OPERATION.Communication language at departure&gt; is not PRESENT
then the Customs system will use the default language of the Office concerned.

**Technical Description**

If /<span>&#42;</span>/TraderAtDestination/communicationLanguageAtDestination is PRESENT, then the indicated<br />
language is used as the basic language in any further communication between the Trader and the<br />
Customs system. If /<span>&#42;</span>/TraderAtDestination/communicationLanguageAtDestination is not PRESENT<br />
then the Customs system will use the default language of the Office concerned;<br />
If /<span>&#42;</span>/TransitOperation/communicationLanguageAtDeparture is PRESENT, then the indicated language<br />
is used as the basic language in any further communication between the Trader and the Customs<br />
system. If /<span>&#42;</span>/TransitOperation/communicationLanguageAtDeparture is not PRESENT then the Customs<br />
system will use the default language of the Office concerned.


## R0102
   
   **Functional Description**
   
   Data item &lt;INVALIDATION.Decision&gt; can contain 2 valid values:
- ‘0’ = ‘No’: Invalidation refused by Customs: Decision
- ‘1’ = ‘Yes’: Invalidation accepted by Customs: Decision
   
   **Technical Description**
   
   Data item /<span>&#42;</span>/Invalidation/decision can contain 2 valid values:<br />
- ‘0’ = ‘No’: Invalidation refused by Customs: Decision<br />
- ‘1’ = ‘Yes’: Invalidation accepted by Customs: Decision
   

## R0103

**Functional Description**

IF &lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)&gt; is PRESENT
THEN
&lt;CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED). Reference number&gt; is NOT EQUAL to
&lt;CUSTOMS OFFICE TRANSIT (DECLARED).Reference number&gt; AND is NOT EQUAL to
&lt;CUSTOMS OFFICE OF DESTINATION (DECLARED).Reference number&gt;

**Technical Description**

IF /<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared is PRESENT<br />
THEN<br />
/<span>&#42;</span>/CustomsOfficeOfExitForTransitDeclared/referenceNumber is NOT EQUAL to<br />
/<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber AND is NOT EQUAL to<br />
/<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber


## R0106

**Functional Description**

&lt;TRANSPORT EQUIPMENT.Number of seals&gt; is EQUAL to the ‘maximum value of &lt;TRANSPORT
EQUIPMENT- SEAL.Sequence number&gt;’ for THIS instance of Transport Equipment.

**Technical Description**

/<span>&#42;</span>/TransportEquipment/numberOfSeals is EQUAL to the ‘maximum value of<br />
/<span>&#42;</span>/TransportEquipment/Seal/sequenceNumber’ for THIS instance of Transport Equipment.


## R0107

**Functional Description**

&lt;TRANSPORT EQUIPMENT-SEAL.Identifier&gt; is unique in the whole declaration.

**Technical Description**

/<span>&#42;</span>/TransportEquipment/Seal/identifier is unique in the whole declaration.

## R0165

**Functional Description**

IF the declaration is submitted under simplified procedure AND the authorisation of which foresees the
use of seals
THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Number of seals&gt; is GREATER than '0'.

**Technical Description**

IF the declaration is submitted under simplified procedure AND the authorisation of which foresees the<br />
use of seals<br />
THEN /<span>&#42;</span>/Consignment/TransportEquipment/numberOfSeals&gt; is GREATER than '0'.


## R0219

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of
packages&gt; is EQUAL to '0' (zero)
THEN no further data group &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-
PACKAGING&gt; with a value not equal to '0' (zero) in the data item &lt;CONSIGNMENT-HOUSE
CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of packages&gt; is specified for this data
group &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt;.

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages is EQUAL to<br />
'0' (zero)<br />
THEN no further data group /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging with a<br />
value not equal to '0' (zero) in the data item<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages is specified for<br />
this data group /<span>&#42;</span>/HouseConsignment/ConsignmentItem.


## R0220

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of
packages&gt; is EQUAL to '0' (zero)
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Type of
packages&gt; shall not be in SET <a href="../downloads/CL182.zip">CL182</a> (KindOfPackagesUnpacked) for this data group
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt;.

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages is EQUAL to<br />
'0' (zero)<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages shall not be<br />
in SET <a href="../downloads/CL182.zip">CL182</a> for this data group /<span>&#42;</span>/ Consignment/HouseConsignment/ConsignmentItem.


## R0221

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of
packages&gt; is EQUAL to ‘0’ (zero)
THEN
  for THIS CONSIGNMENT ITEM
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS
  MEASURE.Gross mass&gt; is EQUAL to ‘0’ (zero)
AND
  for THIS HOUSE CONSIGNMENT at least one other CONSIGNMENT ITEM must exist with
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS
  MEASURE.Gross mass&gt; having a value different from ‘0’ (zero)
ELSE for THIS CONSIGNMENT ITEM
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS
  MEASURE.Gross mass&gt; must be different from ‘0’ (zero).

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages is EQUAL to<br />
‘0’ (zero)<br />
THEN<br />
  for THIS CONSIGNMENT ITEM<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass is<br />
  EQUAL to ‘0’ (zero)<br />
AND<br />
  for THIS HOUSE CONSIGNMENT at least one other CONSIGNMENT ITEM must exist with<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass<br />
  having a value different from ‘0’ (zero)<br />
ELSE for THIS CONSIGNMENT ITEM<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass<br />
  must be different from ‘0’ (zero).


## R0223

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS
MEASURE.Gross mass&gt; is GREATER THAN '0' (zero value).<br /><br />
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS
MEASURE.Net mass&gt; must be LESS THAN OR EQUAL to &lt;CONSIGNMENT-HOUSE
CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS MEASURE.Gross mass&gt;.

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass is<br />
GREATER THAN ‘0’ (zero)<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/netMass<br />
must be LESS THAN OR EQUAL to<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/GoodsMeasure/grossMass.


## R0315

**Functional Description**

Where &lt;CONSIGNMENT.Mode of transport at the border&gt; is EQUAL to '4' the (IATA/ICAO) flight
number shall be indicated and shall have a format an..8:
  - an..3: mandatory prefix identifying the airline/operator
  - n..4: mandatory number of the flight
  - a1: optional suffix

**Technical Description**

Where /<span>&#42;</span>/Consignment/modeOfTransportAtTheBorder is EQUAL to '4' the (IATA/ICAO) flight number<br />
shall be indicated and shall have a format an..8:<br />
  - an..3: mandatory prefix identifying the airline/operator<br />
  - n..4: mandatory number of the flight<br />
  - a1: optional suffix


## R0318

**Functional Description**

IF &lt;GUARANTEE.Guarantee type&gt; is EQUAL to '4'
THEN the format of &lt;GUARANTEE-GUARANTEE REFERENCE.GRN&gt; is 'an24'
ELSE the format of &lt;GUARANTEE-GUARANTEE REFERENCE.GRN&gt; is 'an17'

**Technical Description**

IF /<span>&#42;</span>/Guarantee/guaranteeType is EQUAL to '4'<br />
THEN the format of /<span>&#42;</span>/Guarantee/GuaranteeReference/GRN is 'an24'<br />
ELSE the format of /<span>&#42;</span>/Guarantee/GuaranteeReference/GRN is 'an17'


## R0350

**Functional Description**

IF &lt;TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1'
AND
&lt;CONSIGNMENT.Inland mode of transport&gt; is in SET {1, 2, 4}
THEN
at least one &lt;AUTHORISATION.Type&gt; is EQUAL to 'C524'

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator&gt; is EQUAL to '1'<br />
AND /<span>&#42;</span>/Consignment/inlandModeOfTransport is in SET {1, 2, 4}<br />
THEN<br />
at least one /<span>&#42;</span>/Authorisation/type is EQUAL to 'C524'


## R0352

**Functional Description**

IF &lt;TRANSIT OPERATION.Reduced dataset indicator&gt; is EQUAL to '1'
AND
&lt;CONSIGNMENT.Inland mode of transport&gt; is in SET {1, 2, 4}
THEN
this Data Item includes at least one &lt;Authorisation number&gt; for a valid Authorisation for Reduced Data
Set owned by the Holder of the Transit Procedure

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator&gt; is EQUAL to '1'<br />
AND /<span>&#42;</span>/Consignment/inlandModeOfTransport is in SET {1, 2, 4}<br />
THEN<br />
this Data Item includes at least one &lt;Authorisation number&gt; for a valid Authorisation for Reduced Data<br />
Set owned by the Holder of the Transit Procedure


## R0364

**Functional Description**

IF&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Number of
Packages&gt; is EQUAL to ‘0’ (zero)
THEN for THIS HOUSE CONSIGNMENT at least one other CONSIGNMENT ITEM must exist with
(the same &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Shipping
marks&gt; AND with &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-
PACKAGING.Number of packages&gt; having a value GREATER than ‘0’ (zero) AND
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PACKAGING.Type of packages&gt;
having a value NOT IN SET {<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackagesBulk.zip">CL181</a>(KindOfPackagesBulk), <a href="../downloads/CL182.zip">CL182</a>(KindOfPackagesUnpacked)}).

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages is EQUAL to<br />
‘0’ (zero)<br />
THEN for THIS HOUSE CONSIGNMENT at least one other CONSIGNMENT ITEM must exist with<br />
(the same /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/shippingMarks AND with<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/numberOfPackages having a value<br />
GREATER than ‘0’ (zero) AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Packaging/typeOfPackages having a value<br />
NOT IN SET {<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackagesBulk.zip">CL181</a>, <a href="../downloads/CL182.zip">CL182</a>}).


## R0410

**Functional Description**

IF &lt;CC015C-TRANSIT OPERATION.Security&gt; (the transit declaration includes ENS data for safety
and security purposes [only]) is EQUAL to ‘1’
THEN the 17th character of MRN is EQUAL to 'L'
ELSE IF &lt;TRANSIT OPERATION.Security&gt; (the transit declaration includes EXS data for safety and
security purposes [only]) is EQUAL to ‘2’
THEN the 17th character of MRN is EQUAL to 'K'
ELSE IF &lt;TRANSIT OPERATION.Security&gt; (the transit declaration includes ENS and EXS data for
safety and security purposes [only]) is EQUAL to ‘3’
THEN the 17th character of MRN is EQUAL to 'M'
ELSE the 17th character of MRN is EQUAL to 'J'

**Technical Description**

IF /CC015C/TransitOperation/security (the transit declaration includes ENS data for safety and security<br />
purposes [only]) is EQUAL to ‘1’<br />
THEN the 17th character of MRN is EQUAL to 'L'<br />
ELSE IF /<span>&#42;</span>/TransitOperation/security (the transit declaration includes EXS data for safety and security<br />
purposes [only]) is EQUAL to EQUAL to ‘2’<br />
THEN the 17th character of MRN is EQUAL to 'K'<br />
ELSE IF <span>&#42;</span>/TransitOperation/security (the transit declaration includes ENS and EXS data for safety and<br />
security purposes [only]) is EQUAL to ‘3’<br />
THEN the 17th character of MRN is EQUAL to 'M'<br />
ELSE the 17th character of MRN is EQUAL to 'J'


## R0416

**Functional Description**

The Data Item &lt;CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT. Reference
Number&gt; must include a valid ‘Export declaration’ or an ‘Export and exit summary declaration’ or a
‘Dispatch of goods in relation with special fiscal territories’.

**Technical Description**

The Data Item /<span>&#42;</span>/Consignment/HouseConsignment/PreviousDocument/referenceNumber must include<br />
a valid export MRN. The 17th character must be in SET {A, B, E}.


## R0448

**Functional Description**

IF &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Container identification number&gt; is NOT PRESENT
THEN the value '0' (zero) is not valid for &lt;CONSIGNMENT-TRANSPORT
EQUIPMENT.Number of seals&gt;;
IF &lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Container identification number&gt; is NOT
PRESENT
THEN the value '0' (zero) is not valid for &lt;CONSIGNMENT-INCIDENT-TRANSPORT
EQUIPMENT.Number of seals&gt;

**Technical Description**

IF /<span>&#42;</span>/Consignment/TransportEquipment/containerIdentificationNumber is NOT PRESENT<br />
THEN the value '0' (zero) is not valid for<br />
/<span>&#42;</span>/Consignment/TransportEquipment/numberOfSeals;<br />
IF /<span>&#42;</span>/Consignment/Incident/TransportEquipment/containerIdentificationNumber is NOT PRESENT<br />
THEN the value '0' (zero) is not valid for<br />
/<span>&#42;</span>/Consignment/Incident/TransportEquipment/numberOfSeals


## R0472

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is in SET {1,2,3,4,8}
THEN
   IF &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT
   THEN
  the first digit of &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS.Type of
  identification&gt; shall be EQUAL to &lt;CONSIGNMENT.Inland mode of transport&gt;
   ELSE IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT
   MEANS&gt; is PRESENT
   THEN
  the first digit of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE
  TRANSPORT MEANS.Type of identification&gt; shall be EQUAL to
  &lt;CONSIGNMENT.Inland mode of transport&gt;

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is in SET {1,2,3,4,8}<br />
THEN<br />
  IF /<span>&#42;</span>/Consignment/DepartureTransportMeans is PRESENT<br />
  THEN<br />
the first digit of /<span>&#42;</span>/Consignment/DepartureTransportMeans/typeOfIdentification shall be<br />
EQUAL to /<span>&#42;</span>/Consignment/inlandModeOfTransport<br />
  ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans is PRESENT<br />
  THEN<br />
the first digit of<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans/typeOfIdentification<br />
 shall be EQUAL to /<span>&#42;</span>/Consignment/inlandModeOfTransport


## R0473

**Functional Description**

IF &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT AND
&lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS.Type of identification&gt; is in SET
{10,20,21,30,31,40,41,80}
THEN &lt; CONSIGNMENT-DEPARTURE TRANSPORT MEANS.Identification number&gt; shall not
contain lowercase letters
ELSE IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is
PRESENT AND &lt;CONSIGNMENT- HOUSE CONSIGNMENT-DEPARTURE TRANSPORT
MEANS.Type of identification&gt; is in SET {10,20,21,30,31,40,41,80}
THEN &lt; CONSIGNMENT- HOUSE CONSIGNMENT-DEPARTURE TRANSPORT
MEANS.Identification number&gt; shall not contain lowercase letters

**Technical Description**

IF /<span>&#42;</span>/Consignment/DepartureTransportMeans is PRESENT AND<br />
/<span>&#42;</span>/Consignment/DepartureTransportMeans/typeofIdentification is in SET {10,20,21,30,31,40,41,80}<br />
THEN /<span>&#42;</span>/Consignment/DepartureTransportMeans/IdentificationNumber shall not contain lowercase<br />
letters<br />
ELSE IF /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans is PRESENT AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans/typeofIdentification is in SET<br />
{10,20,21,30,31,40,41,80}<br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans/IdentificationNumber shall not<br />
contain lowercase letters


## R0474

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '3'
THEN the first data group iteration &lt;Consignment-Departure Transport Means.Type of identification&gt;
must be EQUAL to '30';
IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '3'
AND &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT
THEN for THIS House Consignment, the first data group iteration &lt;CONSIGNMENT-HOUSE
CONSIGNMENT-DEPARTURE TRANSPORT MEANS.Type of identification&gt; must be EQUAL to '30'

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '3'<br />
THEN the first data group iteration /<span>&#42;</span>/Consignment/DepartureTransportMeans/typeOfIdentification must<br />
be EQUAL to '30';<br />
IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '3'<br />
AND /<span>&#42;</span>/Consignment/House Consignment/DepartureTransportMeans is PRESENT<br />
THEN for THIS House Consignment, the first data group iteration<br />
/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans/typeOfIdentification must be EQUAL to<br />
'30'.


## R0476

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '3'
THEN
 IF the multiplicity of the data group &lt;CONSIGNMENT-DEPARTURE TRANSPORT
  MEANS&gt; is more than 1x
  THEN the iteration 2 and the iteration 3 (if present) of the data group
 &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; must include
 &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS.Type of identification&gt;
  that is EQUAL to '31'
  ELSE IF the multiplicity of the data group &lt;CONSIGNMENT-HOUSE
  CONSIGNMENT- DEPARTURE TRANSPORT MEANS&gt; is more than 1x
  THEN the iteration 2 and the iteration 3 (if present) of the data group
  &lt;CONSIGNMENT- HOUSE CONSIGNMENT-DEPARTURE TRANSPORT
  MEANS&gt; must include &lt;CONSIGNMENT-HOUSE CONSIGNMENT-
  DEPARTURE TRANSPORT MEANS.Type of identification&gt; that is EQUAL to '31'

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to '3'<br />
THEN<br />
   IF the multiplicity of the data group /<span>&#42;</span>/Consignment/DepartureTransportMeans is<br />
more than 1x<br />
THEN the iteration 2 and the iteration 3 (if present) of the data group<br />
 /<span>&#42;</span>/Consignment/DepartureTransportMeans must include<br />
/<span>&#42;</span>/Consignment/DepartureTransportMeans/typeOfIdentification that is EQUAL to<br />
'31'<br />
ELSE IF the multiplicity of the data group<br />
/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans is more than 1x<br />
THEN the iteration 2 and the iteration 3 (if present) of the data group<br />
/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans must include<br />
/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans/typeOfIdentification<br />
that is EQUAL to '31'


## R0506

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt; is PRESENT for all &lt;CONSIGNMENT-
HOUSE CONSIGNMENT&gt;
THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNOR&gt; must be
different from the others;
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; is PRESENT for all &lt;CONSIGNMENT-
HOUSE CONSIGNMENT&gt;
THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNEE&gt; must be
different from the others;
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is PRESENT
for all &lt;CONSIGNMENT-HOUSE CONSIGNMENT&gt;
THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE
TRANSPORT MEANS&gt; must be different from the others;
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT- TRANSPORT CHARGES&gt; is PRESENT for all
&lt;CONSIGNMENT-HOUSE CONSIGNMENT&gt;
THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT- TRANSPORT
CHARGES&gt; must be different from the others;
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Reference number UCR&gt; is PRESENT for all
&lt;CONSIGNMENT-HOUSE CONSIGNMENT&gt;
THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Reference number
UCR&gt; must be different from the others;
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of dispatch&gt; is PRESENT for all
&lt;CONSIGNMENT-HOUSE CONSIGNMENT&gt;
THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Country of dispatch&gt;
must be different from the others.

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignor is PRESENT for all<br />
/<span>&#42;</span>/Consignment/HouseConsignment/<br />
THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/Consignor must be different from<br />
the others;<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/Consignee is PRESENT for all<br />
/<span>&#42;</span>/Consignment/HouseConsignment/<br />
THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/Consignee must be different<br />
from the others;<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans is PRESENT for all<br />
/<span>&#42;</span>/Consignment/HouseConsignment<br />
THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans must<br />
be different from the others;<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges is PRESENT for all<br />
/<span>&#42;</span>/Consignment/HouseConsignment<br />
THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/TransportCharges must be<br />
different from the others;<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/referenceNumberUCR is PRESENT for all<br />
/<span>&#42;</span>/Consignment/HouseConsignment/<br />
THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/referenceNumberUCR must be<br />
different from the others;<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch is PRESENT for all<br />
/<span>&#42;</span>/Consignment/HouseConsignment/<br />
THEN at least one occurrence of /<span>&#42;</span>/Consignment/HouseConsignment/countryOfDispatch must be<br />
different from the others.


## R0507

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of dispatch&gt; is
PRESENT for all
 &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt;
THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT
ITEM.Country
  of dispatch&gt; must be different from the others;
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country of destination&gt; is
PRESENT for
  all &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt;
THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT
ITEM.Country
  of destination&gt; must be different from the others;
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Reference number UCR&gt; is
PRESENT for
  all &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt;
THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT
ITEM.Reference
  number UCR&gt; must be different from the others;
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM. Declaration type &gt; is
PRESENT for all
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM&gt;
THEN at least one occurrence of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT
  ITEM.Declaration type&gt; must be different from the others.

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch is PRESENT for all<br />
   /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem<br />
THEN at least one occurrence of<br />
   /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDispatch must be different from<br />
the others;<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is PRESENT for all<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem<br />
THEN at least one occurrence of<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination must be different<br />
from the others;<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR is PRESENT for all<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem<br />
THEN at least one occurrence of<br />
 /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/referenceNumberUCR must be different<br />
from the others;<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is PRESENT for all<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem<br />
THEN at least one occurrence of<br />
/<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType must be different from the<br />
others


## R0520

**Functional Description**

IF ( the Data Item &lt;TRANSIT OPERATION.Amendment type flag&gt; is EQUAL to ‘1' and the movement
is in state “Guarantee under amendment”)
(i.e. the message CC013C is used for amending the Guarantee previously declared while the
movement is in state “Guarantee under amendment”)
THEN
the only difference between this CC013C and the CC015C (or the previous CC013C) shall be located
in the Data Group &lt;GUARANTEE&gt;
ELSE
   IF (the Data Item &lt;TRANSIT OPERATION.Amendment type flag&gt; is EQUAL to ‘0' AND the
movement IS NOT IN STATE “Guarantee under amendment”)
  THEN
  all Data Groups and Data Items of the original declaration can be amended, with the exception of
the following Data Groups:
  - &lt;HOLDER OF THE TRANSIT PROCEDURE&gt;
  - &lt;REPRESENTATIVE&gt;
  - &lt;CUSTOMS OFFICE OF DEPARTURE&gt;
  and the exception of the following Data Items:
  - &lt;TRANSIT OPERATION.Additional declaration type&gt;
  - &lt;TRANSIT OPERATION.Declaration type&gt;
  - &lt;TRANSIT OPERATION.MRN&gt;
  - &lt;TRANSIT OPERATION.LRN&gt;
  - &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-
COMMODITY
  CODE. Harmonized System sub-heading code&gt;
  - &lt;TRANSIT OPERATION.Security&gt;

**Technical Description**

IF (the Data Item /CC013C/TransitOperation/amendmentTypeFlag is EQUAL to ‘1' AND the movement<br />
is in state “Guarantee under amendment”)<br />
 (i.e. the message CC013C is used for amending the Guarantee previously declared while the<br />
movement is in state “Guarantee under amendment”)<br />
THEN<br />
the only difference between this CC013C and the CC015C (or the previous CC013C) shall be located<br />
in the Data Group /<span>&#42;</span>/Guarantee<br />
ELSE<br />
 IF (the Data Item /<span>&#42;</span>/TransitOperation/amendmentTypeFlag is EQUAL to ‘0' AND the movement IS<br />
NOT IN STATE “Guarantee under amendment”)<br />
 THEN<br />
 all Data Groups and Data Items of the original declaration can be amended, with the exception of<br />
the following Data Groups:<br />
   - /<span>&#42;</span>/HolderOfTheTransitProcedure<br />
   - /<span>&#42;</span>/Representative<br />
   - /<span>&#42;</span>/CustomsOfficeOfDeparture<br />
 and the exception of the following Data Items:<br />
   - /<span>&#42;</span>/TransitOperation/additionalDeclarationType<br />
   - /<span>&#42;</span>/TransitOperation/declarationType<br />
   - /<span>&#42;</span>/TransitOperation/MRN<br />
   - /<span>&#42;</span>/TransitOperation/LRN<br />
   - /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/Commodity/<br />
 CommodityCode/harmonizedSystemSubHeadingCode<br />
   - /<span>&#42;</span>/TransitOperation/security


## R0601

**Functional Description**

IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL
REFERENCE.Type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a> (DocumentTypeExcise) (i.e. Export of excise goods followed by
transit (EMCS&AES+NCTS)
THEN
   IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT.Type&gt; is EQUAL to ‘N830’
   THEN
 IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is
PRESENT
 THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is
EQUAL to ‘T1’
 ELSE &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T1, TIR}
   ELSE
IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-SUPPORTING
DOCUMENT.Type&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a>
  (DocumentTypeExcise)   (i.e. Transit movement of EU goods under excise suspension
(EMCS+NCTS))
THEN
  IF &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM. Declaration type&gt; is
PRESENT
  THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt;
is in SET {T2, T2F}
  ELSE &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F}

**Technical Description**

IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalReference/type is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a><br />
(DocumentTypeExcise)<br />
(i.e. Export of excise goods followed by transit (EMCS&AES+NCTS))<br />
THEN<br />
   IF /<span>&#42;</span>/Consignment/HouseConsignment/PreviousDocument/type is EQUAL to ‘N830’<br />
   THEN<br />
 IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is PRESENT<br />
 THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is EQUAL to ‘T1’<br />
 ELSE /<span>&#42;</span>/TransitOperation/declarationType is in SET {T1, TIR}<br />
   ELSE<br />
IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/SupportingDocument/type is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL234</a><br />
  (DocumentTypeExcise) (i.e. Transit movement of EU goods under excise suspension<br />
(EMCS+NCTS))<br />
THEN<br />
  IF /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is PRESENT<br />
  THEN /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2,<br />
T2F}<br />
  ELSE /<span>&#42;</span>/TransitOperation/declarationType is in SET {T2, T2F}


## R0789

**Functional Description**

IF &lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; is PRESENT
THEN the multiplicity of &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is up to 9x
ELSE the multiplicity of &lt;CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is 1x

**Technical Description**

IF/<span>&#42;</span>/CustomsOfficeOfTransitDeclared is PRESENT<br />
THEN the multiplicity of /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans is up to 9x<br />
ELSE the multiplicity of /<span>&#42;</span>/Consignment/ActiveBorderTransportMeans is 1x


## R0790

**Functional Description**

IF (&lt;CC015C-CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; is PRESENT)
THEN the multiplicity of &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is up
to 9x
ELSE IF (&lt;CC013C-CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; is PRESENT)
THEN the multiplicity of &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is up
to 9x
ELSE the multiplicity of &lt;CC170C-CONSIGNMENT-ACTIVE BORDER TRANSPORT MEANS&gt; is 1x

**Technical Description**

IF (/CC015C/CustomsOfficeOfTransitDeclared is PRESENT)<br />
THEN the multiplicity of /CC170C/Consignment/ActiveBorderTransportMeans is up to 9x<br />
ELSE IF (/CC013C/CustomsOfficeOfTransitDeclared is PRESENT)<br />
THEN the multiplicity of /CC170C/Consignment/ActiveBorderTransportMeans is up to 9x<br />
ELSE the multiplicity of /CC170C/Consignment/ActiveBorderTransportMeans is 1x


## R0840

**Functional Description**

Only a valid EORI or TCUIN shall be used. The EORI shall be validated only by EU MS. The TCUIN
shall be validated by EU MS and by the country where the TCUIN is defined.

**Technical Description**

Only a valid EORI or TCUIN shall be used. The EORI shall be validated only by EU MS. The TCUIN<br />
shall be validated by EU MS and by the country where the TCUIN is defined.


## R0849

**Functional Description**

IF &lt;TRANSIT OPERATION. Declaration Type&gt; is EQUAL to ‘TIR’
THEN &lt;TRANSIT OPERATION. Reduced Dataset Indicator&gt; = “0”

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to ‘TIR’<br />
THEN /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator = “0”


## R0850

**Functional Description**

IF sender is in EU (<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity))
THEN the value must be a valid EORI or TCUIN (validated by receiver, if located in EU),
ELSE (sender is not in EU) the value must be a TIN number (validated by the message sender only).<br /><br />
The EORI/TCUIN values shall comply with the following pattern: &lt;xs:pattern value=" [A-Z]{2}[\x21-
\x7E]{1,15}"/&gt;

**Technical Description**

IF sender is in EU (<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a>)<br />
THEN the value must be a valid EORI or TCUIN (validated by receiver, if located in EU),<br />
ELSE (sender is not in EU) the value must be a TIN number (validated by the message sender only).<br />
The EORI/TCUIN values shall comply with the following pattern: &lt;xs:pattern value=" [A-Z]{2}[\x21-<br />
\x7E]{1,15}"/&gt;


## R0851

**Functional Description**

The Identification number can be validated if the Consignee is located in the same contracting party as
the Recipient.

**Technical Description**

The Identification number can be validated if the Consignee is located in the same contracting party as<br />
the Recipient.


## R0855

**Functional Description**

IF &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '3'
THEN the multiplicity of &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; AND
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; can be up to '3x'
ELSE IF &lt; CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '2'
THEN the multiplicity of &lt; CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; AND
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; can be more than
'1x'
ELSE the multiplicity of &lt;CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; AND
CONSIGNMENT-HOUSE CONSIGNMENT-DEPARTURE TRANSPORT MEANS&gt; is '1x'

**Technical Description**

IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to ‘3’<br />
THEN the multiplicity of /<span>&#42;</span>/Consignment/DepartureTransportMeans AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans can be up to '3x'<br />
ELSE IF /<span>&#42;</span>/Consignment/inlandModeOfTransport is EQUAL to ‘2’<br />
THEN the multiplicity of /<span>&#42;</span>/Consignment/DepartureTransportMeans AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans can be more than '1x'<br />
ELSE the multiplicity of /<span>&#42;</span>/Consignment/DepartureTransportMeans AND<br />
/<span>&#42;</span>/Consignment/HouseConsignment/DepartureTransportMeans is '1x'


## R0859

**Functional Description**

IF &lt;TRANSIT OPERATION. Reduced Dataset Indicator&gt; = “1”
THEN at least one &lt;AUTHORISATION. Type&gt; is EQUAL to ‘C524’
ELSE &lt;AUTHORISATION. Type&gt; shall not be EQUAL to ‘C524’

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/reducedDatasetIndicator = “1”<br />
THEN at least one /<span>&#42;</span>/Authorisation/type is EQUAL to ‘C524’<br />
ELSE /<span>&#42;</span>/Authorisation/type shall not be EQUAL to ‘C524’


## R0860

**Functional Description**

IF sender is in EU (<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity)),
THEN the value must be a valid EORI or TCUIN,
ELSE (sender is not in EU) the value must be a valid TIN number.

**Technical Description**

IF sender is in EU (<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a>)<br />
THEN the value must be a valid EORI or TCUIN<br />
ELSE (sender is not in EU) the value must be a valid TIN number.


## R0871

**Functional Description**

Reference number assigned must be equal to the one included in CD001C, CD003C, CC013C,
CC015C, CD050C, CD115C, CD160C OR CD165C.

**Technical Description**

Reference number assigned must be equal to the one included in CD001C, CD003C, CC013C,<br />
CC015C, CD050C, CD115C, CD160C OR CD165C.


## R0900

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'
THEN &lt;GUARANTEE.Guarantee type&gt; is EQUAL to 'B'
ELSE IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF
DEPARTURE.Reference number&gt; is in SET of <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity) OR is EQUAL to
'SM' OR is EQUAL to 'AD'
THEN &lt;GUARANTEE.Guarantee type&gt; must be in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeEUNonTIR.zip">CL230</a> (GuaranteeTypeEUNonTIR)
ELSE &lt;GUARANTEE.Guarantee type&gt; must be in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeCTC.zip">CL229</a> (GuaranteeTypeCTC)

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br />
THEN /<span>&#42;</span>/Guarantee/guaranteeType is EQUAL to 'B'<br />
ELSE IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
OR is EQUAL to 'SM' OR is EQUAL to 'AD'<br />
THEN /<span>&#42;</span>/Guarantee/guaranteeType must be in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeEUNonTIR.zip">CL230</a><br />
ELSE /<span>&#42;</span>/Guarantee/guaranteeType must be in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeTypeCTC.zip">CL229</a>


## R0901

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'
THEN the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION
(DECLARED).Reference number&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity)
AND the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference
number &gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity).

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br />
THEN the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
AND the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a>


## R0904

**Functional Description**

IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference
number&gt; is in SET {AD, SM}
THEN the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION
(DECLARED).Reference number&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_MSCountry.zip">CL553</a> (MSCountry)

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET {AD, SM}<br />
THEN the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_MSCountry.zip">CL553</a>


## R0905

**Functional Description**

IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference
number&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a> (CountryCodesCTC)
THEN the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION
(DECLARED).Reference number&gt; is NOT in SET {AD, SM}

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DocumentTypeExcise.zip">CL112</a><br />
THEN the two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is NOT in<br />
SET{AD, SM}


## R0906

**Functional Description**

IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION
(DECLARED).Reference number&gt; is EQUAL to ‘AD’
THEN the country code (first two characters) in the &lt;CUSTOMS OFFICE OF TRANSIT
(DECLARED).Reference number&gt; is EQUAL to ‘AD’;
IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION
(DECLARED).Reference number&gt; is EQUAL to ‘AD’
THEN the country code (first two characters) in the &lt;CUSTOMS OFFICE OF TRANSIT
(ACTUAL).Reference number&gt; is EQUAL to ‘AD’

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is EQUAL to<br />
‘AD’<br />
THEN the first two characters of /<span>&#42;</span>/CustomsOfficeOfTransitDeclared/referenceNumber is EQUAL to<br />
‘AD’;<br />
IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is EQUAL to<br />
‘AD’<br />
THEN the first two characters of /<span>&#42;</span>/CustomsOfficeOfTransitActual/referenceNumber is EQUAL to ‘AD’


## R0909

**Functional Description**

IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION
(DECLARED) Reference number&gt; is EQUAL to 'SM'
THEN
  IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF
DEPARTURE.Reference number&gt; is EQUAL to 'IT'
  THEN &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'T2SM'
  ELSE
 IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF
DEPARTURE.Reference number&gt; is in set <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity) AND NOT EQUAL to
'IT'
 THEN &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F} OR
  &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is
in SET {T2,T2F};
IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DESTINATION (ACTUAL)
Reference number&gt; is EQUAL to 'SM'
THEN
IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF
DEPARTURE.Reference number&gt; is EQUAL to 'IT'
THEN &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'T2SM'
ELSE
 IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF
DEPARTURE.Reference number&gt; is in set <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity) AND NOT EQUAL to
'IT'
 THEN &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F} OR
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Declaration type&gt; is in SET {T2,
T2F}

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is EQUAL to<br />
'SM'<br />
THEN<br />
IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'IT',<br />
THEN /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'T2SM'<br />
ELSE<br />
 IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
 AND NOT EQUAL to 'IT'<br />
 THEN /<span>&#42;</span>/TransitOperation/declarationType is in SET {T2, T2F} OR<br />
   /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2,<br />
T2F};<br />
IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationActual/referenceNumber is EQUAL to 'SM'<br />
THEN<br />
IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'IT',<br />
THEN /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'T2SM'<br />
ELSE<br />
   IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
  AND NOT EQUAL to 'IT'<br />
   THEN /<span>&#42;</span>/TransitOperation/declarationType is in SET {T2, T2F} OR<br />
  /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/declarationType is in SET {T2,<br />
T2F}


## R0910

**Functional Description**

IF &lt;CC013C - AUTHORISATION.Type&gt; is NOT EQUAL to 'C521' OR &lt;CC015C -
AUTHORISATION.Type&gt; is NOT EQUAL to 'C521'
THEN &lt;CONTROL RESULT.Code&gt; is in SET <a href="../downloads/CL195.zip">CL195</a>
(ControlResultCodeDepartureSimplifiedExcluded)

**Technical Description**

IF /CC013C/Authorisation/type is NOT EQUAL to 'C521' OR<br />
/CC015C/Authorisation/type is NOT EQUAL to 'C521'<br />
THEN /<span>&#42;</span>/ControlResult/code is in SET <a href="../downloads/CL195.zip">CL195</a>


## R0911

**Functional Description**

IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference
number&gt; is
  EQUAL to 'SM' AND
  the country code (first two characters) in the &lt;CUSTOMS OFFICE OF
DESTINATION
  (DECLARED).Reference&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity)
THEN &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F};
IF the country code (first two characters) in the &lt;CUSTOMS OFFICE OF DEPARTURE.Reference
number&gt; is
  EQUAL to 'SM' AND
  the country code (first two characters) in the &lt;CUSTOMS OFFICE OF
DESTINATION
  (ACTUAL).Reference&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a> (CountryCodesCommunity)
THEN &lt;TRANSIT OPERATION.Declaration type&gt; is in SET {T2, T2F}

**Technical Description**

IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'SM' AND<br />
 the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationDeclared/referenceNumber is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
THEN /<span>&#42;</span>/TransitOperation/declarationType is in SET {T2, T2F};<br />
IF the first two characters of /<span>&#42;</span>/CustomsOfficeOfDeparture/referenceNumber is EQUAL to 'SM' AND<br />
 the first two characters of /<span>&#42;</span>/CustomsOfficeOfDestinationActual/referenceNumber is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommunity.zip">CL010</a><br />
THEN /<span>&#42;</span>/TransitOperation/declarationType is in SET {T2, T2F}


## R0912

**Functional Description**

IF &lt;TRANSIT OPERATION.Declaration type&gt; is EQUAL to 'TIR'
THEN &lt;CONTROL RESULT.Code&gt; is in SET <a href="../downloads/CL195.zip">CL195</a>
(ControlResultCodeDepartureSimplifiedExcluded)

**Technical Description**

IF /<span>&#42;</span>/TransitOperation/declarationType is EQUAL to 'TIR'<br />
THEN /<span>&#42;</span>/ControlResult/code is in SET <a href="../downloads/CL195.zip">CL195</a>


## R0983

**Functional Description**

&lt;CONSIGNMENT-HOUSE CONSIGNMENT.Gross mass&gt; must be GREATER than OR EQUAL to the
sum of &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-GOODS
MEASURE.Gross mass&gt; available for all Consignment Items included in that House Consignment

**Technical Description**

/<span>&#42;</span>/Consignment/HouseConsignment/grossMass must be GREATER than OR EQUAL to the sum of<br />
/<span>&#42;</span>/Consignment/HouseConsignmentConsignmentItem/Commodity/GoodsMeasure/grossMass available<br />
for all Consignment Items included in that House Consignment


## R0987

**Functional Description**

Each &lt;Sequence number&gt; is unique for the Data Group it belongs to. The sequence numbers shall be
sequential, starting from '1' for the first iteration of the Data Group and increasing by '1' for each
iteration.

**Technical Description**

Each &lt;Sequence number&gt; is unique for the Data Group it belongs to. The sequence numbers shall be<br />
sequential, starting from '1' for the first iteration of the Data Group and increasing by '1' for each<br />
iteration.


## R0988

**Functional Description**

Each &lt; Goods item number&gt; is unique for the Data Group it belongs to. The Goods item number shall
be sequential, starting from '1' for the first iteration of the Data Group and increasing by '1' for each
iteration.

**Technical Description**

Each &lt; Goods item number&gt; is unique for the Data Group it belongs to. The Goods item number shall<br />
be sequential, starting from '1' for the first iteration of the Data Group and increasing by '1' for each<br />
iteration.


## R0990

**Functional Description**

The &lt;TRANSIT OPERATION.TIR carnet number&gt; must have the format an10 or an11 and must follow
the algorithm defined by IRU, see DDNTA Main Document.

**Technical Description**

The /<span>&#42;</span>/TransitOperation/TIRCarnetNumber must have the format an10 or an11 and must follow the<br />
algorithm defined by IRU, see DDNTA Main Document.


## R0994

**Functional Description**

The value of &lt;CONSIGNMENT.Gross mass&gt; must be GREATER than or EQUAL to the sum of
&lt;CONSIGNMENT-HOUSE CONSIGNMENT.Gross mass&gt; for all house consignments.

**Technical Description**

The value of /<span>&#42;</span>/Consignment/grossMass must be GREATER than or EQUAL to the sum of<br />
/<span>&#42;</span>/Consignment/HouseConsignment/grossMass for all house consignments.


## R3060

**Functional Description**

IF &lt;CONSIGNMENT.Country Of Destination&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a> (CountryCodesCommonTransit)
OR
at least one &lt; CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country Of
Destination&gt; are in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a>
THEN &lt;CONSIGNMENT-ADDITIONAL INFORMATION.Code&gt; shall not be EQUAL to '30600'

**Technical Description**

IF /<span>&#42;</span>/Consignment/countryOfDestination is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a><br />
OR<br />
at least one /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a><br />
THEN /<span>&#42;</span>/Consignment/AdditionalInformation/code shall not be EQUAL to '30600'


## R3061

**Functional Description**

The Data Item &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL
INFORMATION.Code&gt; shall not be EQUAL to '30600'

**Technical Description**

The Data Item /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/AdditionalInformation/code shall<br />
not be EQUAL to '30600'


## R3062

**Functional Description**

IF &lt;CONSIGNMENT.Country Of Destination&gt; is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a> (CountryCodesCommonTransit)
OR
at least one &lt; CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM.Country Of
Destination&gt; are in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a>
THEN &lt;CONSIGNMENT-HOUSE CONSIGNMENT- ADDITIONAL INFORMATION.Code&gt; shall not be
EQUAL to '30600'

**Technical Description**

IF /<span>&#42;</span>/Consignment/countryOfDestination is in SET <a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a><br />
OR<br />
at least one /<span>&#42;</span>/Consignment/HouseConsignment/ConsignmentItem/countryOfDestination is in SET<br />
<a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a><br />
THEN /<span>&#42;</span>/Consignment/HouseConsignment/AdditionalInformation/code shall not be EQUAL to '30600'
