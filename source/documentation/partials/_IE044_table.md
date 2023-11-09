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
    <td><a href="rules-g.html#g0002">G0002</a></td>
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
    <td><a href="rules-c.html#c0511">C0511</a><br /><a href="rules-r.html#r0008">R0008</a></td>
</tr><tr>
    <td><strong>- TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-- Other things to report</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>- CUSTOMS OFFICE OF DESTINATION (ACTUAL)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0042">G0042</a></td>
</tr><tr>
    <td>-- Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDestination.zip">CL172</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>- TRADER AT DESTINATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0042">G0042</a></td>
</tr><tr>
    <td>-- Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td><strong>- UNLOADING REMARK</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-- Conform</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td><a href="rules-g.html#g0205">G0205</a></td>
</tr><tr>
    <td>-- Unloading completion</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td><a href="rules-g.html#g0186">G0186</a></td>
</tr><tr>
    <td>-- Unloading date</td>
    <td>R</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-- State of seals</td>
    <td>D</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Flag.zip">CL027</a></td>
    <td><a href="rules-c.html#c0440">C0440</a><br /><a href="rules-g.html#g0017">G0017</a></td>
</tr><tr>
    <td>-- Unloading remark</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>- CONSIGNMENT</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-- Gross mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-- TRANSPORT EQUIPMENT</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0103">G0103</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>--- Container identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Number of seals</td>
    <td>O</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>--- SEAL</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>---- Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0107">R0107</a></td>
</tr><tr>
    <td><strong>--- GOODS REFERENCE</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>---- Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0005">G0005</a><br /><a href="rules-g.html#g0006">G0006</a></td>
</tr><tr>
    <td><strong>-- DEPARTURE TRANSPORT MEANS</strong></td>
    <td>O</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>--- Type of identification</td>
    <td>O</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a></td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Identification number</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Nationality</td>
    <td>O</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-- SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>--- Type</td>
    <td>O</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
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
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>--- Type</td>
    <td>O</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-- ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>--- Type</td>
    <td>O</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-- HOUSE CONSIGNMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>--- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>--- Gross mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>--- DEPARTURE TRANSPORT MEANS</strong></td>
    <td>O</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>---- Type of identification</td>
    <td>O</td>
    <td>n2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TypeOfIdentificationOfMeansOfTransport.zip">CL750</a></td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Identification number</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Nationality</td>
    <td>O</td>
    <td>a2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_Nationality.zip">CL165</a></td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>--- SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>---- Type</td>
    <td>O</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
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
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>---- Type</td>
    <td>O</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>--- ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>---- Type</td>
    <td>O</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>--- CONSIGNMENT ITEM</strong></td>
    <td>O</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>---- Goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0055">R0055</a></td>
</tr><tr>
    <td>---- Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0005">G0005</a><br /><a href="rules-r.html#r0055">R0055</a></td>
</tr><tr>
    <td><strong>---- COMMODITY</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>----- Description of goods</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>----- CUS code</td>
    <td>O</td>
    <td>an9</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CUSCode.zip">CL016</a></td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>----- COMMODITY CODE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
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
    <td><a href="rules-c.html#c0816">C0816</a><br /><a href="rules-g.html#g0360">G0360</a><br /><a href="rules-r.html#r0060">R0060</a></td>
</tr><tr>
    <td><strong>----- GOODS MEASURE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>------ Gross mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>------ Net mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>---- PACKAGING</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>----- Type of packages</td>
    <td>O</td>
    <td>an2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackages.zip">CL017</a></td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>----- Number of packages</td>
    <td>O</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-g.html#g0139">G0139</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>----- Shipping marks</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>---- SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>----- Type</td>
    <td>O</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_SupportingDocumentType.zip">CL213</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>----- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>----- Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>---- TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a><br /><a href="rules-g.html#g0989">G0989</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>----- Type</td>
    <td>O</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_TransportDocumentType.zip">CL754</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>----- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>---- ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>----- Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>----- Type</td>
    <td>O</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_AdditionalReference.zip">CL380</a></td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>----- Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a><br /><a href="rules-r.html#r0023">R0023</a></td>
</tr></table>