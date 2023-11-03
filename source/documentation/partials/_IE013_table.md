<table cellspacing="0">
<tr>
<th>
   Field Name
  </th>
<th>
   Priority
  </th>
<th>
   Format / Max Repeat
  </th>
<th>
   Code Lists
  </th>
<th>
   Rules
  </th>
</tr>
<tr>
    <td><strong>MESSAGE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>- Message sender</td>
    <td>R</td>
    <td>an..35 (see <a href="../#message-sender-and-recipient-guidelines">Message sender and recipient guidelines</a>)</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>- Message recipient</td>
    <td>R</td>
    <td>an..35 (see <a href="../#message-sender-and-recipient-guidelines">Message sender and recipient guidelines</a>)</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>- Preparation date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td>- Message identification</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>- Message type</td>
    <td>R</td>
    <td>an6</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_MessageTypes.zip">CL060</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>- Correlation identifier</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1833</a><br /><a href="rules-c.html">C0511</a><br /><a href="rules-r.html">R0008</a></td>
</tr><tr>
    <td><strong>- TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- LRN</td>
    <td>D</td>
    <td>an..22</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0467</a></td>
</tr><tr>
    <td>-- MRN</td>
    <td>D</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0467</a><br /><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td>-- Declaration type</td>
    <td>R</td>
    <td>an..5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationType.zip">CL231</a></td>
    <td><a href="rules-b.html">B1922</a><br /><a href="rules-r.html">R0601</a><br /><a href="rules-r.html">R0909</a><br /><a href="rules-r.html">R0911</a></td>
</tr><tr>
    <td>-- Additional declaration type</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeAdditional.zip">CL042</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- TIR Carnet number</td>
    <td>D</td>
    <td>an..12</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0411</a><br /><a href="rules-r.html">R0990</a></td>
</tr><tr>
    <td>-- Presentation of the goods date and time</td>
    <td>O</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td>-- Security</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeSecurity.zip">CL217</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Reduced dataset indicator</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td><a href="rules-r.html">R0849</a></td>
</tr><tr>
    <td>-- Specific circumstance indicator</td>
    <td>O</td>
    <td>an3</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SpecificCircumstanceIndicatorCode.zip">CL296</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Communication language at departure</td>
    <td>O</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_LanguageByCustoms.zip">CL192</a></td>
    <td><a href="rules-r.html">R0100</a></td>
</tr><tr>
    <td>-- Binding itinerary</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Amendment type flag</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td><a href="rules-r.html">R0520</a></td>
</tr><tr>
    <td>-- Limit date</td>
    <td>D</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0839</a><br /><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td><strong>- AUTHORISATION</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0101</a><br /><a href="rules-g.html">G0102</a><br /><a href="rules-g.html">G0167</a></td>
</tr><tr>
    <td>-- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>-- Type</td>
    <td>R</td>
    <td>an..4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AuthorisationTypeDeparture.zip">CL235</a></td>
    <td><a href="rules-g.html">G0114</a><br /><a href="rules-g.html">G0117</a><br /><a href="rules-r.html">R0350</a><br /><a href="rules-r.html">R0859</a></td>
</tr><tr>
    <td>-- Reference number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0033</a><br /><a href="rules-r.html">R0352</a></td>
</tr><tr>
    <td><strong>- CUSTOMS OFFICE OF DEPARTURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDeparture.zip">CL171</a></td>
    <td><a href="rules-r.html">R0901</a></td>
</tr><tr>
    <td><strong>- CUSTOMS OFFICE OF DESTINATION (DECLARED)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0034</a></td>
</tr><tr>
    <td>-- Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDestination.zip">CL172</a></td>
    <td><a href="rules-r.html">R0901</a><br /><a href="rules-r.html">R0904</a><br /><a href="rules-r.html">R0905</a></td>
</tr><tr>
    <td><strong>- CUSTOMS OFFICE OF TRANSIT (DECLARED)</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0030</a><br /><a href="rules-g.html">G0030</a></td>
</tr><tr>
    <td>-- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>-- Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeTransit.zip">CL173</a></td>
    <td><a href="rules-b.html">B1813</a><br /><a href="rules-g.html">G0142</a><br /><a href="rules-r.html">R0003</a><br /><a href="rules-r.html">R0006</a><br /><a href="rules-r.html">R0906</a></td>
</tr><tr>
    <td>-- Arrival date and time (estimated)</td>
    <td>D</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1831</a><br /><a href="rules-b.html">B1904</a><br /><a href="rules-c.html">C0598</a><br /><a href="rules-g.html">G0002</a><br /><a href="rules-r.html">R0005</a></td>
</tr><tr>
    <td><strong>- CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0587</a><br /><a href="rules-g.html">G0587</a></td>
</tr><tr>
    <td>-- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>-- Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeTransitExit.zip">CL175</a></td>
    <td><a href="rules-r.html">R0103</a></td>
</tr><tr>
    <td><strong>- HOLDER OF THE TRANSIT PROCEDURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0120</a><br /><a href="rules-r.html">R0850</a></td>
</tr><tr>
    <td>-- TIR holder identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0904</a><br /><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td>-- Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a><br /><a href="rules-e.html">E1104</a></td>
</tr><tr>
    <td><strong>-- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a></td>
</tr><tr>
    <td>--- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1104</a></td>
</tr><tr>
    <td>--- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0505</a><br /><a href="rules-e.html">E1102</a></td>
</tr><tr>
    <td>--- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0105</a></td>
</tr><tr>
    <td>--- Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td><strong>- REPRESENTATIVE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0850</a></td>
</tr><tr>
    <td>-- Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0850</a></td>
</tr><tr>
    <td>-- Status</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_RepresentativeStatusCode.zip">CL094</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0105</a></td>
</tr><tr>
    <td>--- Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td><strong>- GUARANTEE</strong></td>
    <td>R</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>-- Guarantee type</td>
    <td>O</td>
    <td>an1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeType.zip">CL251</a></td>
    <td><a href="rules-r.html">R0900</a></td>
</tr><tr>
    <td>-- Other guarantee reference</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0130</a></td>
</tr><tr>
    <td><strong>-- GUARANTEE REFERENCE</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0085</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- GRN</td>
    <td>D</td>
    <td>an..24</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0086</a><br /><a href="rules-g.html">G0002</a><br /><a href="rules-r.html">R0318</a></td>
</tr><tr>
    <td>--- Access code</td>
    <td>D</td>
    <td>an..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0086</a><br /><a href="rules-e.html">E1118</a></td>
</tr><tr>
    <td>--- Amount to be covered</td>
    <td>O</td>
    <td>n..16,2</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B2101</a><br /><a href="rules-g.html">G0021</a></td>
</tr><tr>
    <td>--- Currency</td>
    <td>O</td>
    <td>a3</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CurrencyCodes.zip">CL048</a></td>
    <td><a href="rules-b.html">B1898</a><br /><a href="rules-b.html">B2101</a></td>
</tr><tr>
    <td><strong>- CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html">C0909</a><br /><a href="rules-g.html">G0988</a></td>
</tr><tr>
    <td>-- Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html">C0343</a></td>
</tr><tr>
    <td>-- Container indicator</td>
    <td>D</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td><a href="rules-c.html">C0822</a><br /><a href="rules-g.html">G0332</a></td>
</tr><tr>
    <td>-- Inland mode of transport</td>
    <td>O</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportModeCode.zip">CL218</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Mode of transport at the border</td>
    <td>D</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportModeCode.zip">CL218</a></td>
    <td><a href="rules-b.html">B1889</a><br /><a href="rules-c.html">C0599</a><br /><a href="rules-g.html">G0020</a><br /><a href="rules-g.html">G0115</a></td>
</tr><tr>
    <td>-- Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1109</a><br /><a href="rules-r.html">R0994</a></td>
</tr><tr>
    <td>-- Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1895</a><br /><a href="rules-c.html">C0502</a><br /><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td><strong>-- CARRIER</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0090</a></td>
</tr><tr>
    <td>--- Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a><br /><a href="rules-g.html">G0201</a><br /><a href="rules-r.html">R0840</a></td>
</tr><tr>
    <td><strong>--- CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0105</a></td>
</tr><tr>
    <td>---- Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td><strong>-- CONSIGNOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0542</a><br /><a href="rules-g.html">G0123</a></td>
</tr><tr>
    <td>--- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0850</a></td>
</tr><tr>
    <td>--- Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a><br /><a href="rules-e.html">E1104</a></td>
</tr><tr>
    <td><strong>--- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a></td>
</tr><tr>
    <td>---- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1104</a></td>
</tr><tr>
    <td>---- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0505</a><br /><a href="rules-e.html">E1102</a></td>
</tr><tr>
    <td>---- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0105</a></td>
</tr><tr>
    <td>---- Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td><strong>-- CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1823</a><br /><a href="rules-c.html">C0001</a><br /><a href="rules-g.html">G0001</a></td>
</tr><tr>
    <td>--- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0851</a></td>
</tr><tr>
    <td>--- Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a><br /><a href="rules-e.html">E1104</a></td>
</tr><tr>
    <td><strong>--- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a></td>
</tr><tr>
    <td>---- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1104</a></td>
</tr><tr>
    <td>---- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0505</a><br /><a href="rules-e.html">E1102</a></td>
</tr><tr>
    <td>---- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Role</td>
    <td>R</td>
    <td>a..3</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalSupplyChainActorRoleCode.zip">CL704</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a><br /><a href="rules-g.html">G0201</a><br /><a href="rules-r.html">R0840</a></td>
</tr><tr>
    <td><strong>-- TRANSPORT EQUIPMENT</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0823</a><br /><a href="rules-g.html">G0103</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0055</a><br /><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td>--- Number of seals</td>
    <td>R</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1832</a><br /><a href="rules-g.html">G0021</a><br /><a href="rules-r.html">R0106</a><br /><a href="rules-r.html">R0165</a><br /><a href="rules-r.html">R0448</a></td>
</tr><tr>
    <td><strong>--- SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0569</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0107</a></td>
</tr><tr>
    <td><strong>--- GOODS REFERENCE</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0670</a><br /><a href="rules-g.html">G0670</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0005</a><br /><a href="rules-g.html">G0006</a></td>
</tr><tr>
    <td><strong>-- LOCATION OF GOODS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1804</a><br /><a href="rules-c.html">C0710</a></td>
</tr><tr>
    <td>--- Type of location</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfLocation.zip">CL347</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Qualifier of identification</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_QualifierOfTheIdentification.zip">CL326</a></td>
    <td><a href="rules-g.html">G0500</a></td>
</tr><tr>
    <td>--- Authorisation number</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td>--- Additional identifier</td>
    <td>D</td>
    <td>an..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0671</a></td>
</tr><tr>
    <td>--- UN LOCODE</td>
    <td>D</td>
    <td>an..17</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnLocodeExtended.zip">CL244</a></td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td><strong>--- CUSTOMS OFFICE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td>---- Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDeparture.zip">CL171</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- GNSS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td>---- Latitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a><br /><a href="rules-g.html">G0014</a></td>
</tr><tr>
    <td>---- Longitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a><br /><a href="rules-g.html">G0014</a></td>
</tr><tr>
    <td><strong>--- ECONOMIC OPERATOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td>---- Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0850</a></td>
</tr><tr>
    <td><strong>--- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td>---- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1104</a></td>
</tr><tr>
    <td>---- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0505</a><br /><a href="rules-e.html">E1102</a></td>
</tr><tr>
    <td>---- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- POSTCODE ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a></td>
</tr><tr>
    <td>---- House number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0382</a></td>
</tr><tr>
    <td>---- Postcode</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryAddressPostcodeBased.zip">CL190</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- CONTACT PERSON</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0394</a><br /><a href="rules-g.html">G0105</a></td>
</tr><tr>
    <td>---- Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td><strong>-- DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1890</a><br /><a href="rules-b.html">B1891</a><br /><a href="rules-c.html">C0826</a><br /><a href="rules-g.html">G0088</a><br /><a href="rules-g.html">G0119</a><br /><a href="rules-r.html">R0855</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Type of identification</td>
    <td>O</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a></td>
    <td><a href="rules-b.html">B1091</a><br /><a href="rules-b.html">B1892</a><br /><a href="rules-b.html">B2101</a><br /><a href="rules-g.html">G0112</a><br /><a href="rules-r.html">R0472</a><br /><a href="rules-r.html">R0474</a><br /><a href="rules-r.html">R0476</a></td>
</tr><tr>
    <td>--- Identification number</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1815</a><br /><a href="rules-b.html">B1892</a><br /><a href="rules-b.html">B2101</a><br /><a href="rules-e.html">E1103</a><br /><a href="rules-r.html">R0473</a></td>
</tr><tr>
    <td>--- Nationality</td>
    <td>O</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td><a href="rules-b.html">B1897</a><br /><a href="rules-b.html">B2101</a></td>
</tr><tr>
    <td><strong>-- COUNTRY OF ROUTING OF CONSIGNMENT</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1848</a><br /><a href="rules-c.html">C0586</a><br /><a href="rules-g.html">G0061</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- ACTIVE BORDER TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1806</a><br /><a href="rules-c.html">C0806</a><br /><a href="rules-e.html">E1406</a><br /><a href="rules-g.html">G0118</a><br /><a href="rules-r.html">R0789</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Customs office at border reference number</td>
    <td>O</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/COL-Generic-20230601.zip">CL141</a></td>
    <td><a href="rules-b.html">B1016</a><br /><a href="rules-b.html">B2101</a><br /><a href="rules-g.html">G0789</a></td>
</tr><tr>
    <td>--- Type of identification</td>
    <td>O</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationofMeansOfTransportActive.zip">CL219</a></td>
    <td><a href="rules-b.html">B1838</a><br /><a href="rules-b.html">B2101</a><br /><a href="rules-g.html">G0112</a></td>
</tr><tr>
    <td>--- Identification number</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1811</a><br /><a href="rules-b.html">B1838</a><br /><a href="rules-b.html">B2101</a><br /><a href="rules-e.html">E1103</a><br /><a href="rules-r.html">R0076</a></td>
</tr><tr>
    <td>--- Nationality</td>
    <td>O</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td><a href="rules-b.html">B1850</a><br /><a href="rules-b.html">B2101</a></td>
</tr><tr>
    <td>--- Conveyance reference number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0531</a><br /><a href="rules-g.html">G0002</a><br /><a href="rules-r.html">R0315</a></td>
</tr><tr>
    <td><strong>-- PLACE OF LOADING</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1893</a><br /><a href="rules-c.html">C0403</a></td>
</tr><tr>
    <td>--- UN LOCODE</td>
    <td>O</td>
    <td>an..17</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnLocodeExtended.zip">CL244</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Country</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html">C0387</a></td>
</tr><tr>
    <td>--- Location</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0387</a><br /><a href="rules-e.html">E1114</a></td>
</tr><tr>
    <td><strong>-- PLACE OF UNLOADING</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1858</a><br /><a href="rules-c.html">C0191</a></td>
</tr><tr>
    <td>--- UN LOCODE</td>
    <td>O</td>
    <td>an..17</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnLocodeExtended.zip">CL244</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Country</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html">C0387</a></td>
</tr><tr>
    <td>--- Location</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0387</a></td>
</tr><tr>
    <td><strong>-- PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentType.zip">CL214</a></td>
    <td><a href="rules-g.html">G0057</a><br /><a href="rules-r.html">R0020</a></td>
</tr><tr>
    <td>--- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0321</a></td>
</tr><tr>
    <td>--- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html">G0057</a></td>
</tr><tr>
    <td>--- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0321</a></td>
</tr><tr>
    <td>--- Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>--- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html">G0057</a></td>
</tr><tr>
    <td>--- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0321</a></td>
</tr><tr>
    <td><strong>-- ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html">G0057</a></td>
</tr><tr>
    <td>--- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0321</a></td>
</tr><tr>
    <td><strong>-- ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Code</td>
    <td>R</td>
    <td>an5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalInformation.zip">CL239</a></td>
    <td><a href="rules-g.html">G0057</a><br /><a href="rules-r.html">R3060</a></td>
</tr><tr>
    <td>--- Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- TRANSPORT CHARGES</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0186</a></td>
</tr><tr>
    <td>--- Method of payment</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportChargesMethodOfPayment.zip">CL116</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-- HOUSE CONSIGNMENT</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1406</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>--- Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html">C0909</a><br /><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0988</a><br /><a href="rules-r.html">R0506</a></td>
</tr><tr>
    <td>--- Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0983</a></td>
</tr><tr>
    <td>--- Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0502</a><br /><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0002</a><br /><a href="rules-r.html">R0506</a></td>
</tr><tr>
    <td><strong>--- CONSIGNOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0542</a><br /><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0123</a><br /><a href="rules-r.html">R0506</a></td>
</tr><tr>
    <td>---- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0850</a></td>
</tr><tr>
    <td>---- Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a></td>
</tr><tr>
    <td><strong>---- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a></td>
</tr><tr>
    <td>----- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0505</a></td>
</tr><tr>
    <td>----- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>---- CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0105</a></td>
</tr><tr>
    <td>----- Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a></td>
</tr><tr>
    <td><strong>--- CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0001</a><br /><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0001</a><br /><a href="rules-r.html">R0506</a></td>
</tr><tr>
    <td>---- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0851</a></td>
</tr><tr>
    <td>---- Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a></td>
</tr><tr>
    <td><strong>---- ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0250</a></td>
</tr><tr>
    <td>----- Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0505</a></td>
</tr><tr>
    <td>----- City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Role</td>
    <td>R</td>
    <td>a..3</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalSupplyChainActorRoleCode.zip">CL704</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a><br /><a href="rules-g.html">G0201</a><br /><a href="rules-r.html">R0840</a></td>
</tr><tr>
    <td><strong>--- DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0826</a><br /><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0088</a><br /><a href="rules-g.html">G0119</a><br /><a href="rules-r.html">R0506</a><br /><a href="rules-r.html">R0855</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a></td>
    <td><a href="rules-g.html">G0112</a><br /><a href="rules-r.html">R0472</a><br /><a href="rules-r.html">R0474</a><br /><a href="rules-r.html">R0476</a></td>
</tr><tr>
    <td>---- Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0473</a></td>
</tr><tr>
    <td>---- Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0026</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Type</td>
    <td>R</td>
    <td>an4</td>
    <td>CL228</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0416</a></td>
</tr><tr>
    <td>---- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html">G0057</a></td>
</tr><tr>
    <td>---- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0321</a></td>
</tr><tr>
    <td>---- Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>---- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html">G0057</a></td>
</tr><tr>
    <td>---- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0321</a></td>
</tr><tr>
    <td><strong>--- ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html">G0057</a></td>
</tr><tr>
    <td>---- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0321</a></td>
</tr><tr>
    <td><strong>--- ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1301</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>---- Code</td>
    <td>R</td>
    <td>an5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalInformation.zip">CL239</a></td>
    <td><a href="rules-g.html">G0057</a><br /><a href="rules-r.html">R3062</a></td>
</tr><tr>
    <td>---- Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- TRANSPORT CHARGES</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0186</a><br /><a href="rules-c.html">C0337</a><br /><a href="rules-e.html">E1301</a><br /><a href="rules-r.html">R0506</a></td>
</tr><tr>
    <td>---- Method of payment</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportChargesMethodOfPayment.zip">CL116</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>--- CONSIGNMENT ITEM</strong></td>
    <td>R</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0071</a></td>
</tr><tr>
    <td>---- Goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0072</a><br /><a href="rules-r.html">R0988</a></td>
</tr><tr>
    <td>---- Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0005</a><br /><a href="rules-r.html">R0007</a></td>
</tr><tr>
    <td>---- Declaration type</td>
    <td>D</td>
    <td>an..5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeItemLevel.zip">CL232</a></td>
    <td><a href="rules-b.html">B1922</a><br /><a href="rules-c.html">C0045</a><br /><a href="rules-r.html">R0507</a><br /><a href="rules-r.html">R0601</a><br /><a href="rules-r.html">R0909</a></td>
</tr><tr>
    <td>---- Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html">C0909</a><br /><a href="rules-g.html">G0988</a><br /><a href="rules-r.html">R0507</a></td>
</tr><tr>
    <td>---- Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html">C0343</a><br /><a href="rules-r.html">R0507</a></td>
</tr><tr>
    <td>---- Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1895</a><br /><a href="rules-c.html">C0502</a><br /><a href="rules-g.html">G0002</a><br /><a href="rules-r.html">R0507</a></td>
</tr><tr>
    <td><strong>---- CONSIGNEE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1820</a><br /><a href="rules-b.html">B1877</a><br /><a href="rules-b.html">B2400</a><br /><a href="rules-g.html">G0001</a></td>
</tr><tr>
    <td>----- Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0851</a></td>
</tr><tr>
    <td>----- Name</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1821</a><br /><a href="rules-e.html">E1104</a></td>
</tr><tr>
    <td><strong>----- ADDRESS</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1821</a></td>
</tr><tr>
    <td>------ Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1104</a></td>
</tr><tr>
    <td>------ Postcode</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1822</a><br /><a href="rules-e.html">E1102</a></td>
</tr><tr>
    <td>------ City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>------ Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>---- ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>----- Role</td>
    <td>R</td>
    <td>a..3</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalSupplyChainActorRoleCode.zip">CL704</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0002</a><br /><a href="rules-g.html">G0201</a><br /><a href="rules-r.html">R0840</a></td>
</tr><tr>
    <td><strong>---- COMMODITY</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Description of goods</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1107</a></td>
</tr><tr>
    <td>----- CUS code</td>
    <td>O</td>
    <td>an9</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CUSCode.zip">CL016</a></td>
    <td><a href="rules-g.html">G0301</a></td>
</tr><tr>
    <td><strong>----- COMMODITY CODE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1834</a><br /><a href="rules-c.html">C0153</a></td>
</tr><tr>
    <td>------ Harmonized System sub-heading code</td>
    <td>R</td>
    <td>an6</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_HScode.zip">CL152</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>------ Combined nomenclature code</td>
    <td>D</td>
    <td>an2</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0821</a><br /><a href="rules-r.html">R0060</a></td>
</tr><tr>
    <td><strong>----- DANGEROUS GOODS</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1406</a><br /><a href="rules-g.html">G0300</a></td>
</tr><tr>
    <td>------ Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>------ UN Number</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnDangerousGoodsCode.zip">CL101</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>----- GOODS MEASURE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B2101</a></td>
</tr><tr>
    <td>------ Gross mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1860</a><br /><a href="rules-b.html">B2101</a><br /><a href="rules-e.html">E1109</a><br /><a href="rules-g.html">G0021</a><br /><a href="rules-r.html">R0221</a></td>
</tr><tr>
    <td>------ Net mass</td>
    <td>D</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1805</a><br /><a href="rules-b.html">B1862</a><br /><a href="rules-c.html">C0837</a><br /><a href="rules-e.html">E1109</a><br /><a href="rules-r.html">R0223</a></td>
</tr><tr>
    <td>------ Supplementary units</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>---- PACKAGING</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>----- Type of packages</td>
    <td>R</td>
    <td>an2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackages.zip">CL017</a></td>
    <td><a href="rules-b.html">B1919</a><br /><a href="rules-r.html">R0220</a></td>
</tr><tr>
    <td>----- Number of packages</td>
    <td>D</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1819</a><br /><a href="rules-b.html">B1964</a><br /><a href="rules-c.html">C0060</a><br /><a href="rules-e.html">E1111</a><br /><a href="rules-g.html">G0021</a><br /><a href="rules-r.html">R0219</a><br /><a href="rules-r.html">R0364</a></td>
</tr><tr>
    <td>----- Shipping marks</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0060</a><br /><a href="rules-e.html">E1105</a><br /><a href="rules-g.html">G0024</a></td>
</tr><tr>
    <td><strong>---- PREVIOUS DOCUMENT</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1000</a><br /><a href="rules-c.html">C0035</a><br /><a href="rules-e.html">E1401</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>----- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentType.zip">CL214</a></td>
    <td><a href="rules-g.html">G0057</a><br /><a href="rules-r.html">R0020</a></td>
</tr><tr>
    <td>----- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1104</a><br /><a href="rules-g.html">G0321</a></td>
</tr><tr>
    <td>----- Goods item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0058</a></td>
</tr><tr>
    <td>----- Type of packages</td>
    <td>O</td>
    <td>an2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackages.zip">CL017</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Number of packages</td>
    <td>O</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Measurement unit and qualifier</td>
    <td>D</td>
    <td>an..4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Unit.zip">CL349</a></td>
    <td><a href="rules-c.html">C0298</a></td>
</tr><tr>
    <td>----- Quantity</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1117</a></td>
</tr><tr>
    <td><strong>---- SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1407</a><br /><a href="rules-g.html">G0069</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>----- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html">G0057</a></td>
</tr><tr>
    <td>----- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1104</a><br /><a href="rules-g.html">G0321</a><br /><a href="rules-g.html">G0414</a></td>
</tr><tr>
    <td>----- Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>----- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1117</a></td>
</tr><tr>
    <td><strong>---- TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1896</a><br /><a href="rules-b.html">B2400</a><br /><a href="rules-e.html">E1407</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>----- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html">G0057</a></td>
</tr><tr>
    <td>----- Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1104</a><br /><a href="rules-g.html">G0321</a></td>
</tr><tr>
    <td><strong>---- ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html">E1407</a><br /><a href="rules-g.html">G0068</a><br /><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>----- Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html">G0057</a></td>
</tr><tr>
    <td>----- Reference number</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html">C0015</a><br /><a href="rules-e.html">E1104</a><br /><a href="rules-g.html">G0050</a><br /><a href="rules-g.html">G0321</a><br /><a href="rules-g.html">G0424</a><br /><a href="rules-r.html">R0023</a></td>
</tr><tr>
    <td><strong>---- ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html">G0825</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html">R0987</a></td>
</tr><tr>
    <td>----- Code</td>
    <td>R</td>
    <td>an5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalInformation.zip">CL239</a></td>
    <td><a href="rules-b.html">B1814</a><br /><a href="rules-g.html">G0057</a><br /><a href="rules-r.html">R3061</a></td>
</tr><tr>
    <td>----- Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>---- TRANSPORT CHARGES</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html">B1875</a><br /><a href="rules-b.html">B1877</a><br /><a href="rules-b.html">B2400</a></td>
</tr><tr>
    <td>----- Method of payment</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportChargesMethodOfPayment.zip">CL116</a></td>
    <td>&nbsp;</td>
</tr></table>