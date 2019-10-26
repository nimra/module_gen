function kda_top () {
var path=kpath + 'aps/';
var ts=new Date().getTime();
var ms=new Date().getMilliseconds();
var Top_nam=new Array(); var Top_ext=new Array(); var Top_wid=new Array(); var Top_hgt=new Array();
var Top_alt=new Array(); var Top_txt=new Array(); var Top_url=new Array(); var Top_wgt=new Array(); var wgt=0;
wgt+=1; Top_wgt[1]=wgt;
Top_nam[1]="t-que-19m07-gmma"; Top_ext[1]=".jpg"; Top_wid[1]=750; Top_hgt[1]=100;
Top_url[1]='https://smith.queensu.ca/grad_studies/mma/program/global-mma/landing.php?utm_source=KDNuggetsBanner&utm_medium=Display&utm_content=GMMA&utm_campaign=GMMA2021';
Top_txt[1]="Global Master of Management Analytics: The Essential Degree for the World of Data";
Top_alt[1]="txt";
wgt+=1; Top_wgt[2]=wgt;
Top_nam[2]="t-jmp-19m01-berry"; Top_ext[2]=".jpg"; Top_wid[2]=750; Top_hgt[2]=100;
Top_url[2]='https://www.jmp.com/en_us/offers/data-mining-techniques-book.html?utm_source=kdnuggetshp&utm_medium=advertisement&utm_campaign=wp701a0000000t5sD';
Top_txt[2]="<font size=+1>Derived Variables: Making the data mean more - Download a free book chapter</font>";
Top_alt[2]="JMP";
wgt+=1; Top_wgt[3]=wgt;
Top_nam[3]="t-paw-19m10-bizde"; Top_ext[3]=".jpg"; Top_wid[3]=750; Top_hgt[3]=100;
Top_url[3]='https://predictiveanalyticsworld.de/de/?utm_source=kdnbanner';
Top_txt[3]="PAW Business, 18-19 November, Berlin. The Premier Machine Learning Conference";
Top_alt[3]="txt";
wgt+=1; Top_wgt[4]=wgt;
Top_nam[4]="t-spe-19m09-ngdl"; Top_ext[4]=".jpg"; Top_wid[4]=750; Top_hgt[4]=100;
Top_url[4]='https://spell.run';
Top_txt[4]="Next Generation Deep Learning Platform - Learn more at spell.run";
Top_alt[4]="txt";
wgt+=1; Top_wgt[5]=wgt;
Top_nam[5]="t-arg-19m08-datax-nyc"; Top_ext[5]=".jpg"; Top_wid[5]=750; Top_hgt[5]=100;
Top_url[5]='https://www.theinnovationenterprise.com/summits/datax-new-york/?source=PSHIPKD';
Top_txt[5]="DATAx New York City - Data Science in the real world. Use KD200 to save";
Top_alt[5]="txt";
var rtop=Math.random()*5;
var n_ad=1; while (Top_wgt[n_ad]<rtop) {n_ad++};
var out='<table border=0 cellspacing=5 cellpadding=20 width=990><tr><td valign=top align=center width=750>';
  if (Top_wid[n_ad] == 1) {
      out+=Top_url[n_ad];
  } else {
      out+='<a href=' + Top_url[n_ad] + ' onclick="ga(\'send\',\'pageview\',\'/zt/' + Top_nam[n_ad] + '\');" target=_blank>';
  }
  var whb=' width="90%" border=0';
  out+='<img src=' + path + Top_nam[n_ad] + Top_ext[n_ad] + '?ms=' + ms + whb + ' alt="' + Top_alt[n_ad] + '">';
  out+='<br><b>' + Top_txt[n_ad] + '</b></a></td>';
  out+='</tr></table><br>';document.writeln(out);}
function kda_sid_init() {
var ts=new Date().getTime();
Sid_nam=new Array(); Sid_ext=new Array(); Sid_txt=new Array(); Sid_url=new Array();
Sid_alt=new Array(); Sid_wid=new Array(); Sid_hgt=new Array(); Sid_wgt=new Array(); var wgt=0;
wgt+=1; Sid_wgt[1]=wgt;
Sid_nam[1]="e-sas-19m10-ai"; Sid_ext[1]=".gif"; Sid_wid[1]=1; Sid_hgt[1]=1;
Sid_url[1]='<ins class="dcmads" style="display:inline-block;width:300px;height:250px" data-dcm-placement="N6626.289580.KDNUGGETS.COM/B22096016.257104691" data-dcm-rendering-mode="iframe" data-dcm-https-only data-dcm-resettable-device-id="" data-dcm-app-id=""> <script src="https://www.googletagservices.com/dcm/dcmads.js"></script> </ins>';
Sid_txt[1]="SAS<br>Brings AI and Analytics<br>to the Cloud";
Sid_alt[1]="SAS";
wgt+=1; Sid_wgt[2]=wgt;
Sid_nam[2]="e-bra-19m10-msba"; Sid_ext[2]=".gif"; Sid_wid[2]=1; Sid_hgt[2]=1;
Sid_url[2]='<ins class="dcmads" style="display:inline-block;width:300px;height:250px" data-dcm-placement="N636.2008108KDNUGGETS/B22904808.258035099" data-dcm-rendering-mode="iframe" data-dcm-https-only data-dcm-resettable-device-id="" data-dcm-app-id="">  <script src="https://www.googletagservices.com/dcm/dcmads.js"></script></ins>';
Sid_txt[2]="Be a next big thinker<br>Get MS in Business Analytics<br>from Brandeis - Learn more";
Sid_alt[2]="Brandeis MSBA";
wgt+=1; Sid_wgt[3]=wgt;
Sid_nam[3]="e-dom-19m10-mlvs"; Sid_ext[3]=".jpg"; Sid_wid[3]=300; Sid_hgt[3]=250;
Sid_url[3]='https://www.brighttalk.com/webcast/17563/373152?utm_source=kdnuggets&utm_medium=display&utm_campaign=373152';
Sid_txt[3]="Machine Learning Vital Signs<br>Oct 23 Webinar<br>Register Now";
Sid_alt[3]="Machine Learning Vital Signs Oct 23 Webinar<br>Register Now";
wgt+=1; Sid_wgt[4]=wgt;
Sid_nam[4]="e-pny-19m10-wbr"; Sid_ext[4]=".jpg"; Sid_wid[4]=300; Sid_hgt[4]=250;
Sid_url[4]='https://pny.zoom.us/webinar/register/9115683953009/WN_2Q82JZEzSjG87MUaTclwOA';
Sid_txt[4]="Attend the live webinar<br>to be entered into a drawing<br>for an NVIDIA Quadro RTX 4000!";
Sid_alt[4]="Attend the live webinar to be entered into a drawing<br>for an NVIDIA Quadro RTX 4000!";
wgt+=1; Sid_wgt[5]=wgt;
Sid_nam[5]="e-kni-19m04-fall"; Sid_ext[5]=".jpg"; Sid_wid[5]=300; Sid_hgt[5]=250;
Sid_url[5]='https://www.knime.com/about/events/knime-fall-summit-2019-austin?kd0319';
Sid_txt[5]="KNIME Fall Summit 2019<br>Nov 5-8, Austin<br>Use code KDNUGGETS for 10% off";
Sid_alt[5]="text";
wgt+=0.5; Sid_wgt[6]=wgt;
Sid_nam[6]="e-tdw-19m10-orl-mdl"; Sid_ext[6]=".jpg"; Sid_wid[6]=300; Sid_hgt[6]=250;
Sid_url[6]='https://tdwi.org/events/conferences/orlando/home.aspx?utm_source=in+house&utm_medium=email&utm_campaign=Orlando2019';
Sid_txt[6]="TDWI Orlando, Nov 10-15. Machine & Deep Learning.";
Sid_alt[6]="TDWI Orlando, Nov 10-15. Machine & Deep Learning.";
wgt+=0.5; Sid_wgt[7]=wgt;
Sid_nam[7]="e-tdw-19m10-orl-ss"; Sid_ext[7]=".jpg"; Sid_wid[7]=300; Sid_hgt[7]=250;
Sid_url[7]='https://tdwi.org/events/strategy-summits/orlando/home.aspx?utm_source=in+house&utm_medium=email&utm_campaign=Orlando2019';
Sid_txt[7]="TDWI Orlando, Nov 11-12. Strategy Summit for Data Management.";
Sid_alt[7]="TDWI Orlando, Nov 11-12. Strategy Summit for Data Management.";
}
function kda_sid_write (nads) {
  var path=kpath + 'aps/';
  var ms=new Date().getMilliseconds(); var adshown=new Array();
  for (adpos=1; adpos<=nads; adpos++) {
    do { var adn=1; var re=Math.random()*6;
      while (Sid_wgt[adn]<re) {adn++};
    } while (adshown[adn]==1);
    if (Sid_wid[adn]==1) { s=Sid_url[adn]; s=s.replace('ze/e-','ze/' + nads + adpos + ':e-'); 
      s+='<img src=' + path + Sid_nam[adn] + '.gif?ms' + ms + ' width=1 height=1 border=0>';
    } else {
      s='<a href=' + Sid_url[adn] + ' onclick="ga(\'send\',\'pageview\',\'/ze/' + nads + adpos + ':' + Sid_nam[adn] + '\');" target=_blank>';
      s+='<img src=' + path + Sid_nam[adn] + Sid_ext[adn] + '?ms' + ms +  ' width=' + Sid_wid[adn] + ' height=' + Sid_hgt[adn] + ' border=0 alt="' + Sid_alt[adn] + '">';}
    s+='<br><b>' + Sid_txt[adn] + '</b></a><br>';
    if (nads>1) {s+='<br><hr class="grey-line"><br>'};
    document.writeln(s); adshown[adn]=1;
  }
}
