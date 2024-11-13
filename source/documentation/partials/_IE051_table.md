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
    <td>-&nbsp;-&nbsp; Declaration submission date and time</td>
    <td>R</td>
    <td>an19</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; No release motivation code</td>
    <td>R</td>
    <td>an2</td>
    <td>CL211</td>
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp; No release motivation text</td>
    <td>R</td>
    <td>an..512</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
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
    <td>CL171</td>
    <td>&nbsp;</td>
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
    <td><a href="rules-c.html#c0250">C0250</a></td>
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
    <td>&nbsp;</td>
</tr><tr>
    <td>-&nbsp;-&nbsp;-&nbsp; Postcode</td>
    <td>D</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-c.html#c0505">C0505</a></td>
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
    <td>CL248</td>
    <td>&nbsp;</td>
</tr><tr>
    <td><strong>-&nbsp; REPRESENTATIVE</strong></td>
    <td>O</td>
    <td>1x</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0860">G0860</a></td>
</tr><tr>
    <td>-&nbsp;-&nbsp; Identification number</td>
    <td>R</td>
    <td>an..17</td>
    <td>&nbsp;</td>
    <td><a href="rules-g.html#g0002">G0002</a></td>
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
</tr></table>