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
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp; Message recipient</td>
    <td>R</td>
    <td>an..35</td>
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
    <td>CL060</td>
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
    <td>-&nbsp;-&nbsp; Other things to report</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp; CUSTOMS OFFICE OF DESTINATION (ACTUAL)</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0042">G0042</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Reference number</td>
    <td>R</td>
    <td>an8</td>
    <td>CL172</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp; TRADER AT DESTINATION</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0042">G0042</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0850">R0850</a></td>
</tr><tr>
    <td><strong>-&nbsp; UNLOADING REMARK</strong></td>
    <td>R</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Conform</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="rules-g.html#g0205">G0205</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Unloading completion</td>
    <td>R</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="rules-g.html#g0186">G0186</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Unloading date</td>
    <td>R</td>
    <td>an10</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; State of seals</td>
    <td>D</td>
    <td>n1</td>
    <td>CL027</td>
    <td><a href="rules-c.html#c0440">C0440</a><br /><a href="rules-g.html#g0017">G0017</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Unloading remark</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp; CONSIGNMENT</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Gross mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; TRANSPORT EQUIPMENT</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0103">G0103</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Container identification number</td>
    <td>O</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Number of seals</td>
    <td>O</td>
    <td>n..4</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; SEAL</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Identifier</td>
    <td>R</td>
    <td>an..20</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0107">R0107</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; GOODS REFERENCE</strong></td>
    <td>O</td>
    <td>9999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Declaration goods item number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0005">G0005</a><br /><a href="rules-g.html#g0006">G0006</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; DEPARTURE TRANSPORT MEANS</strong></td>
    <td>O</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type of identification</td>
    <td>O</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Nationality</td>
    <td>O</td>
    <td>a2</td>
    <td>CL165</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
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
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp; HOUSE CONSIGNMENT</strong></td>
    <td>O</td>
    <td>1999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Gross mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; DEPARTURE TRANSPORT MEANS</strong></td>
    <td>O</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type of identification</td>
    <td>O</td>
    <td>n2</td>
    <td>CL750</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Identification number</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Nationality</td>
    <td>O</td>
    <td>a2</td>
    <td>CL165</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
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
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp; CONSIGNMENT ITEM</strong></td>
    <td>O</td>
    <td>999x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
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
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; COMMODITY</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Description of goods</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; CUS code</td>
    <td>O</td>
    <td>an9</td>
    <td>CL016</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; COMMODITY CODE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Harmonized System sub-heading code</td>
    <td>R</td>
    <td>an6</td>
    <td>CL152</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Combined nomenclature code</td>
    <td>D</td>
    <td>an2</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0816">C0816</a><br /><a href="rules-g.html#g0360">G0360</a><br /><a href="rules-r.html#r0060">R0060</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; GOODS MEASURE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Gross mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Net mass</td>
    <td>O</td>
    <td>n..16,6</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; PACKAGING</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type of packages</td>
    <td>O</td>
    <td>an2</td>
    <td>CL017</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Number of packages</td>
    <td>O</td>
    <td>n..8</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0021">G0021</a><br /><a href="rules-g.html#g0139">G0139</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Shipping marks</td>
    <td>O</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; SUPPORTING DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL213</td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Complement of information</td>
    <td>O</td>
    <td>an..35</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; TRANSPORT DOCUMENT</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a><br /><a href="rules-g.html#g0989">G0989</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL754</td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td><strong>-&nbsp;-&nbsp;-&nbsp;-&nbsp; ADDITIONAL REFERENCE</strong></td>
    <td>O</td>
    <td>99x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Sequence number</td>
    <td>R</td>
    <td>n..5</td>
    <td>&nbsp;</td>
    <td><a href="rules-r.html#r0054">R0054</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Type</td>
    <td>O</td>
    <td>an4</td>
    <td>CL380</td>
    <td><a href="rules-g.html#g0057">G0057</a><br /><a href="rules-g.html#g0360">G0360</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp;-&nbsp;-&nbsp; Reference number</td>
    <td>O</td>
    <td>an..70</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0321">G0321</a><br /><a href="rules-g.html#g0360">G0360</a><br /><a href="rules-r.html#r0023">R0023</a></td>
</tr></table>