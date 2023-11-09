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
    <td><a href="rules-c.html#c0511">C0511</a><br /><a href="rules-r.html#r0008">R0008</a></td>
</tr><tr>
    <td><strong>-&nbsp; TRANSIT OPERATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; MRN</td>
    <td>R</td>
    <td>an18</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Release date</td>
    <td>R</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Release indicator</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_ReleaseNotification.zip">CL164</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp; CUSTOMS OFFICE OF DESTINATION (ACTUAL)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CustomsOfficeDestination.zip">CL172</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp; TRADER AT DESTINATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td><strong>-&nbsp; CONSIGNMENT</strong></td>
    <td>D</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0352">C0352</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; HOUSE CONSIGNMENT</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Release type</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_ReleaseType.zip">CL163</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; CONSIGNMENT ITEM</strong></td>
    <td>D</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0353">C0353</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0055">R0055</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0005">G0005</a><br /><a href="rules-r.html#r0055">R0055</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Release type</td>
    <td>R</td>
    <td>n1</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_ReleaseType.zip">CL163</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; COMMODITY</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0131">G0131</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Description of goods</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; CUS code</td>
    <td>O</td>
    <td>an9</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_CUSCode.zip">CL016</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; COMMODITY CODE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Harmonized System sub-heading code</td>
    <td>R</td>
    <td>an6</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_HScode.zip">CL152</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Combined nomenclature code</td>
    <td>O</td>
    <td>an2</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0060">R0060</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; DANGEROUS GOODS</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0300">G0300</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; UN Number</td>
    <td>R</td>
    <td>an4</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_UnDangerousGoodsCode.zip">CL101</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; GOODS MEASURE</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Gross mass</td>
    <td>R</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-r.html#r0221">R0221</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Net mass</td>
    <td>D</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0844">C0844</a><br /><a href="rules-r.html#r0223">R0223</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; PACKAGING</strong></td>
    <td>R</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0131">G0131</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type of packages</td>
    <td>R</td>
    <td>an2</td>
    <td><a href="https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download/RD_NCTS-P5_KindOfPackages.zip">CL017</a></td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Number of packages</td>
    <td>D</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0060">C0060</a><br /><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-r.html#r0364">R0364</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Shipping marks</td>
    <td>D</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0060">C0060</a><br /><a href="rules-g.html#g0024">G0024</a></td>
</tr></table>