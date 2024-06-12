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
    <td>-&nbsp; Message sender</td>
    <td>R</td>
    <td>an..35 (see <a href="../#message-sender-and-recipient-guidelines">Message sender and recipient guidelines</a>)</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Message recipient</td>
    <td>R</td>
    <td>an..35 (see <a href="../#message-sender-and-recipient-guidelines">Message sender and recipient guidelines</a>)</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Preparation date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp; Message identification</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Message type</td>
    <td>R</td>
    <td>an6</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_MessageTypes.zip">CL060</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Correlation identifier</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1833">B1833</a><br /><a href="rules-c.html#c0511">C0511</a><br /><a href="rules-r.html#r0008">R0008</a></td>
</tr><tr>
    <td><strong>-&nbsp; TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; LRN</td>
    <td>R</td>
    <td>an..22</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Declaration type</td>
    <td>R</td>
    <td>an..5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationType.zip">CL231</a></td>
    <td><a href="rules-b.html#b1922">B1922</a><br /><a href="rules-r.html#r0601">R0601</a><br /><a href="rules-r.html#r0909">R0909</a><br /><a href="rules-r.html#r0911">R0911</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Additional declaration type</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeAdditional.zip">CL042</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; TIR Carnet number</td>
    <td>D</td>
    <td>an..12</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0411">C0411</a><br /><a href="rules-r.html#r0990">R0990</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Presentation of the goods date and time</td>
    <td>O</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Security</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeSecurity.zip">CL217</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reduced dataset indicator</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td><a href="rules-r.html#r0849">R0849</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Specific circumstance indicator</td>
    <td>O</td>
    <td>an3</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SpecificCircumstanceIndicatorCode.zip">CL296</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Communication language at departure</td>
    <td>O</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_LanguageByCustoms.zip">CL192</a></td>
    <td><a href="rules-r.html#r0100">R0100</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Binding itinerary</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Limit date</td>
    <td>D</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0839">C0839</a><br /><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td><strong>-&nbsp; AUTHORISATION</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0101">C0101</a><br /><a href="rules-g.html#g0102">G0102</a><br /><a href="rules-g.html#g0167">G0167</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an..4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AuthorisationTypeDeparture.zip">CL235</a></td>
    <td><a href="rules-g.html#g0114">G0114</a><br /><a href="rules-g.html#g0117">G0117</a><br /><a href="rules-r.html#r0350">R0350</a><br /><a href="rules-r.html#r0859">R0859</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0033">G0033</a><br /><a href="rules-r.html#r0352">R0352</a></td>
</tr><tr>
    <td><strong>-&nbsp; CUSTOMS OFFICE OF DEPARTURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDeparture.zip">CL171</a></td>
    <td><a href="rules-r.html#r0901">R0901</a></td>
</tr><tr>
    <td><strong>-&nbsp; CUSTOMS OFFICE OF DESTINATION (DECLARED)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0034">G0034</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDestination.zip">CL172</a></td>
    <td><a href="rules-r.html#r0901">R0901</a><br /><a href="rules-r.html#r0904">R0904</a><br /><a href="rules-r.html#r0905">R0905</a></td>
</tr><tr>
    <td><strong>-&nbsp; CUSTOMS OFFICE OF TRANSIT (DECLARED)</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0030">C0030</a><br /><a href="rules-g.html#g0030">G0030</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeTransit.zip">CL173</a></td>
    <td><a href="rules-b.html#b1813">B1813</a><br /><a href="rules-g.html#g0142">G0142</a><br /><a href="rules-r.html#r0003">R0003</a><br /><a href="rules-r.html#r0006">R0006</a><br /><a href="rules-r.html#r0906">R0906</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Arrival date and time (estimated)</td>
    <td>D</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1831">B1831</a><br /><a href="rules-b.html#b1904">B1904</a><br /><a href="rules-c.html#c0598">C0598</a><br /><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-r.html#r0005">R0005</a></td>
</tr><tr>
    <td><strong>-&nbsp; CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0587">C0587</a><br /><a href="rules-g.html#g0587">G0587</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeTransitExit.zip">CL175</a></td>
    <td><a href="rules-r.html#r0103">R0103</a></td>
</tr><tr>
    <td><strong>-&nbsp; HOLDER OF THE TRANSIT PROCEDURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0120">G0120</a><br /><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; TIR holder identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0904">C0904</a><br /><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a><br /><a href="rules-e.html#e1104">E1104</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1104">E1104</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a><br /><a href="rules-e.html#e1102">E1102</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0105">G0105</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td><strong>-&nbsp; REPRESENTATIVE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0850">G0850</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Status</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_RepresentativeStatusCode.zip">CL094</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0105">G0105</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td><strong>-&nbsp; GUARANTEE</strong></td>
    <td>R</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Guarantee type</td>
    <td>R</td>
    <td>an1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_GuaranteeType.zip">CL251</a></td>
    <td><a href="rules-r.html#r0900">R0900</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Other guarantee reference</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0130">C0130</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; GUARANTEE REFERENCE</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0085">C0085</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; GRN</td>
    <td>D</td>
    <td>an..24</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0086">C0086</a><br /><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-r.html#r0318">R0318</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Access code</td>
    <td>D</td>
    <td>an..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0086">C0086</a><br /><a href="rules-e.html#e1118">E1118</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Amount to be covered</td>
    <td>O</td>
    <td>n..16,2</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b2101">B2101</a><br /><a href="rules-g.html#g0021">G0021</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Currency</td>
    <td>O</td>
    <td>a3</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CurrencyCodes.zip">CL048</a></td>
    <td><a href="rules-b.html#b1898">B1898</a><br /><a href="rules-b.html#b2101">B2101</a></td>
</tr><tr>
    <td><strong>-&nbsp; CONSIGNMENT</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html#c0909">C0909</a><br /><a href="rules-g.html#g0988">G0988</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html#c0343">C0343</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Container indicator</td>
    <td>D</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td><a href="rules-c.html#c0822">C0822</a><br /><a href="rules-g.html#g0332">G0332</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Inland mode of transport</td>
    <td>O</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportModeCode.zip">CL218</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Mode of transport at the border</td>
    <td>D</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportModeCode.zip">CL218</a></td>
    <td><a href="rules-b.html#b1889">B1889</a><br /><a href="rules-c.html#c0599">C0599</a><br /><a href="rules-g.html#g0020">G0020</a><br /><a href="rules-g.html#g0115">G0115</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1109">E1109</a><br /><a href="rules-r.html#r0994">R0994</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1895">B1895</a><br /><a href="rules-c.html#c0502">C0502</a><br /><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; CARRIER</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0090">G0090</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-g.html#g0201">G0201</a><br /><a href="rules-r.html#r0840">R0840</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0105">G0105</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; CONSIGNOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0542">C0542</a><br /><a href="rules-g.html#g0123">G0123</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a><br /><a href="rules-e.html#e1104">E1104</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1104">E1104</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a><br /><a href="rules-e.html#e1102">E1102</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0105">G0105</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1823">B1823</a><br /><a href="rules-c.html#c0001">C0001</a><br /><a href="rules-g.html#g0001">G0001</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0851">R0851</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a><br /><a href="rules-e.html#e1104">E1104</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1104">E1104</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a><br /><a href="rules-e.html#e1102">E1102</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Role</td>
    <td>R</td>
    <td>a..3</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalSupplyChainActorRoleCode.zip">CL704</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-g.html#g0201">G0201</a><br /><a href="rules-r.html#r0840">R0840</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; TRANSPORT EQUIPMENT</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0823">C0823</a><br /><a href="rules-g.html#g0103">G0103</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Container identification number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0055">C0055</a><br /><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Number of seals</td>
    <td>R</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1832">B1832</a><br /><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-r.html#r0106">R0106</a><br /><a href="rules-r.html#r0165">R0165</a><br /><a href="rules-r.html#r0448">R0448</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; SEAL</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0569">C0569</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0107">R0107</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; GOODS REFERENCE</strong></td>
    <td>D</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0670">C0670</a><br /><a href="rules-g.html#g0670">G0670</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0005">G0005</a><br /><a href="rules-g.html#g0006">G0006</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; LOCATION OF GOODS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1804">B1804</a><br /><a href="rules-c.html#c0710">C0710</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type of location</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfLocation.zip">CL347</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Qualifier of identification</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_QualifierOfTheIdentification.zip">CL326</a></td>
    <td><a href="rules-g.html#g0500">G0500</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Authorisation number</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Additional identifier</td>
    <td>D</td>
    <td>an..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0671">C0671</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; UN LOCODE</td>
    <td>D</td>
    <td>an..17</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnLocodeExtended.zip">CL244</a></td>
    <td><a href="rules-c.html#c0394">C0394</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; CUSTOMS OFFICE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDeparture.zip">CL171</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; GNSS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Latitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-g.html#g0014">G0014</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Longitude</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-g.html#g0014">G0014</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; ECONOMIC OPERATOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1104">E1104</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a><br /><a href="rules-e.html#e1102">E1102</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesCommonTransit.zip">CL009</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; POSTCODE ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0394">C0394</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; House number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0382">C0382</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Postcode</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryAddressPostcodeBased.zip">CL190</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; CONTACT PERSON</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0394">C0394</a><br /><a href="rules-g.html#g0105">G0105</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1890">B1890</a><br /><a href="rules-b.html#b1891">B1891</a><br /><a href="rules-c.html#c0826">C0826</a><br /><a href="rules-g.html#g0088">G0088</a><br /><a href="rules-g.html#g0119">G0119</a><br /><a href="rules-r.html#r0855">R0855</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type of identification</td>
    <td>O</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a></td>
    <td><a href="rules-b.html#b1091">B1091</a><br /><a href="rules-b.html#b1892">B1892</a><br /><a href="rules-b.html#b2101">B2101</a><br /><a href="rules-g.html#g0112">G0112</a><br /><a href="rules-r.html#r0472">R0472</a><br /><a href="rules-r.html#r0474">R0474</a><br /><a href="rules-r.html#r0476">R0476</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1815">B1815</a><br /><a href="rules-b.html#b1892">B1892</a><br /><a href="rules-b.html#b2101">B2101</a><br /><a href="rules-e.html#e1103">E1103</a><br /><a href="rules-r.html#r0473">R0473</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Nationality</td>
    <td>O</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td><a href="rules-b.html#b1897">B1897</a><br /><a href="rules-b.html#b2101">B2101</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; COUNTRY OF ROUTING OF CONSIGNMENT</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1848">B1848</a><br /><a href="rules-c.html#c0586">C0586</a><br /><a href="rules-g.html#g0061">G0061</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; ACTIVE BORDER TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>9x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1806">B1806</a><br /><a href="rules-c.html#c0806">C0806</a><br /><a href="rules-e.html#e1406">E1406</a><br /><a href="rules-g.html#g0118">G0118</a><br /><a href="rules-r.html#r0789">R0789</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Customs office at border reference number</td>
    <td>O</td>
    <td>an8</td>
    <td><a href="../downloads/COL-Generic-20240612.zip">CL141</a></td>
    <td><a href="rules-b.html#b1016">B1016</a><br /><a href="rules-b.html#b2101">B2101</a><br /><a href="rules-g.html#g0789">G0789</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type of identification</td>
    <td>O</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationofMeansOfTransportActive.zip">CL219</a></td>
    <td><a href="rules-b.html#b1838">B1838</a><br /><a href="rules-b.html#b2101">B2101</a><br /><a href="rules-g.html#g0112">G0112</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1811">B1811</a><br /><a href="rules-b.html#b1838">B1838</a><br /><a href="rules-b.html#b2101">B2101</a><br /><a href="rules-e.html#e1103">E1103</a><br /><a href="rules-r.html#r0076">R0076</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Nationality</td>
    <td>O</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td><a href="rules-b.html#b1850">B1850</a><br /><a href="rules-b.html#b2101">B2101</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Conveyance reference number</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0531">C0531</a><br /><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-r.html#r0315">R0315</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; PLACE OF LOADING</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1893">B1893</a><br /><a href="rules-c.html#c0403">C0403</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; UN LOCODE</td>
    <td>O</td>
    <td>an..17</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnLocodeExtended.zip">CL244</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html#c0387">C0387</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Location</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0387">C0387</a><br /><a href="rules-e.html#e1114">E1114</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; PLACE OF UNLOADING</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1858">B1858</a><br /><a href="rules-c.html#c0191">C0191</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; UN LOCODE</td>
    <td>O</td>
    <td>an..17</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnLocodeExtended.zip">CL244</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html#c0387">C0387</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Location</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0387">C0387</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentType.zip">CL214</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-r.html#r0020">R0020</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Code</td>
    <td>R</td>
    <td>an5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalInformation.zip">CL239</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-r.html#r3060">R3060</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; TRANSPORT CHARGES</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0186">C0186</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Method of payment</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportChargesMethodOfPayment.zip">CL116</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; HOUSE CONSIGNMENT</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1406">E1406</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html#c0909">C0909</a><br /><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0988">G0988</a><br /><a href="rules-r.html#r0506">R0506</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0983">R0983</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0502">C0502</a><br /><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-r.html#r0506">R0506</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; CONSIGNOR</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0542">C0542</a><br /><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0123">G0123</a><br /><a href="rules-r.html#r0506">R0506</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; CONTACT PERSON</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0105">G0105</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Phone number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; E-mail address</td>
    <td>O</td>
    <td>an..256</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; CONSIGNEE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0001">C0001</a><br /><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0001">G0001</a><br /><a href="rules-r.html#r0506">R0506</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0851">R0851</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; ADDRESS</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0250">C0250</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Role</td>
    <td>R</td>
    <td>a..3</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalSupplyChainActorRoleCode.zip">CL704</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-g.html#g0201">G0201</a><br /><a href="rules-r.html#r0840">R0840</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; DEPARTURE TRANSPORT MEANS</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0826">C0826</a><br /><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0088">G0088</a><br /><a href="rules-g.html#g0119">G0119</a><br /><a href="rules-r.html#r0506">R0506</a><br /><a href="rules-r.html#r0855">R0855</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type of identification</td>
    <td>R</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a></td>
    <td><a href="rules-g.html#g0112">G0112</a><br /><a href="rules-r.html#r0472">R0472</a><br /><a href="rules-r.html#r0474">R0474</a><br /><a href="rules-r.html#r0476">R0476</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0473">R0473</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Nationality</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; PREVIOUS DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0026">G0026</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentExportType.zip">CL228</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0416">R0416</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Code</td>
    <td>R</td>
    <td>an5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalInformation.zip">CL239</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-r.html#r3062">R3062</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; TRANSPORT CHARGES</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0186">C0186</a><br /><a href="rules-c.html#c0337">C0337</a><br /><a href="rules-e.html#e1301">E1301</a><br /><a href="rules-r.html#r0506">R0506</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Method of payment</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportChargesMethodOfPayment.zip">CL116</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; CONSIGNMENT ITEM</strong></td>
    <td>R</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0071">G0071</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0072">G0072</a><br /><a href="rules-r.html#r0988">R0988</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0005">G0005</a><br /><a href="rules-r.html#r0007">R0007</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Declaration type</td>
    <td>D</td>
    <td>an..5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_DeclarationTypeItemLevel.zip">CL232</a></td>
    <td><a href="rules-b.html#b1922">B1922</a><br /><a href="rules-c.html#c0045">C0045</a><br /><a href="rules-r.html#r0507">R0507</a><br /><a href="rules-r.html#r0601">R0601</a><br /><a href="rules-r.html#r0909">R0909</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Country of dispatch</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html#c0909">C0909</a><br /><a href="rules-g.html#g0988">G0988</a><br /><a href="rules-r.html#r0507">R0507</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Country of destination</td>
    <td>D</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesFullList.zip">CL008</a></td>
    <td><a href="rules-c.html#c0343">C0343</a><br /><a href="rules-r.html#r0507">R0507</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number UCR</td>
    <td>D</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1895">B1895</a><br /><a href="rules-c.html#c0502">C0502</a><br /><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-r.html#r0507">R0507</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; CONSIGNEE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1820">B1820</a><br /><a href="rules-b.html#b1877">B1877</a><br /><a href="rules-b.html#b2400">B2400</a><br /><a href="rules-g.html#g0001">G0001</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0851">R0851</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Name</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1821">B1821</a><br /><a href="rules-e.html#e1104">E1104</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; ADDRESS</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1821">B1821</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Street and number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1104">E1104</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Postcode</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1822">B1822</a><br /><a href="rules-e.html#e1102">E1102</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; City</td>
    <td>R</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Country</td>
    <td>R</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CountryCodesForAddress.zip">CL248</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; ADDITIONAL SUPPLY CHAIN ACTOR</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Role</td>
    <td>R</td>
    <td>a..3</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalSupplyChainActorRoleCode.zip">CL704</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-g.html#g0201">G0201</a><br /><a href="rules-r.html#r0840">R0840</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; COMMODITY</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Description of goods</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1107">E1107</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; CUS code</td>
    <td>O</td>
    <td>an9</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CUSCode.zip">CL016</a></td>
    <td><a href="rules-g.html#g0301">G0301</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; COMMODITY CODE</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1834">B1834</a><br /><a href="rules-c.html#c0153">C0153</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Harmonized System sub-heading code</td>
    <td>R</td>
    <td>an6</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_HScode.zip">CL152</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Combined nomenclature code</td>
    <td>D</td>
    <td>an2</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0821">C0821</a><br /><a href="rules-r.html#r0060">R0060</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; DANGEROUS GOODS</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1406">E1406</a><br /><a href="rules-g.html#g0300">G0300</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; UN Number</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnDangerousGoodsCode.zip">CL101</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; GOODS MEASURE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b2101">B2101</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Gross mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1860">B1860</a><br /><a href="rules-b.html#b2101">B2101</a><br /><a href="rules-e.html#e1109">E1109</a><br /><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-r.html#r0221">R0221</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Net mass</td>
    <td>D</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1805">B1805</a><br /><a href="rules-b.html#b1862">B1862</a><br /><a href="rules-c.html#c0837">C0837</a><br /><a href="rules-e.html#e1109">E1109</a><br /><a href="rules-r.html#r0223">R0223</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Supplementary units</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; PACKAGING</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type of packages</td>
    <td>R</td>
    <td>an2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackages.zip">CL017</a></td>
    <td><a href="rules-b.html#b1919">B1919</a><br /><a href="rules-r.html#r0220">R0220</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Number of packages</td>
    <td>D</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1819">B1819</a><br /><a href="rules-b.html#b1964">B1964</a><br /><a href="rules-c.html#c0060">C0060</a><br /><a href="rules-e.html#e1111">E1111</a><br /><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-r.html#r0219">R0219</a><br /><a href="rules-r.html#r0364">R0364</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Shipping marks</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0060">C0060</a><br /><a href="rules-e.html#e1105">E1105</a><br /><a href="rules-g.html#g0024">G0024</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; PREVIOUS DOCUMENT</strong></td>
    <td>D</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1000">B1000</a><br /><a href="rules-c.html#c0035">C0035</a><br /><a href="rules-e.html#e1401">E1401</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_PreviousDocumentType.zip">CL214</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-r.html#r0020">R0020</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1104">E1104</a><br /><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Goods item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0058">G0058</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type of packages</td>
    <td>O</td>
    <td>an2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackages.zip">CL017</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Number of packages</td>
    <td>O</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Measurement unit and qualifier</td>
    <td>D</td>
    <td>an..4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Unit.zip">CL349</a></td>
    <td><a href="rules-c.html#c0298">C0298</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Quantity</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1117">E1117</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1407">E1407</a><br /><a href="rules-g.html#g0069">G0069</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1104">E1104</a><br /><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0414">G0414</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Document line item number</td>
    <td>O</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1117">E1117</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1896">B1896</a><br /><a href="rules-b.html#b2400">B2400</a><br /><a href="rules-e.html#e1407">E1407</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1104">E1104</a><br /><a href="rules-g.html#g0321">G0321</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-e.html#e1407">E1407</a><br /><a href="rules-g.html#g0068">G0068</a><br /><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html#g0057">G0057</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>D</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0015">C0015</a><br /><a href="rules-e.html#e1104">E1104</a><br /><a href="rules-g.html#g0050">G0050</a><br /><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0424">G0424</a><br /><a href="rules-r.html#r0023">R0023</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; ADDITIONAL INFORMATION</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0825">G0825</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0987">R0987</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Code</td>
    <td>R</td>
    <td>an5</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalInformation.zip">CL239</a></td>
    <td><a href="rules-b.html#b1814">B1814</a><br /><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-r.html#r3061">R3061</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Text</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; TRANSPORT CHARGES</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-b.html#b1875">B1875</a><br /><a href="rules-b.html#b1877">B1877</a><br /><a href="rules-b.html#b2400">B2400</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Method of payment</td>
    <td>R</td>
    <td>a1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportChargesMethodOfPayment.zip">CL116</a></td>
    <td>&nbsp;</td>
</tr></table>