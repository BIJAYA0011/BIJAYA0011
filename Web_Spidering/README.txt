Simple Python Search Spider, Page Ranker, and Visualizer

This is a set of programs that emulate some of the functions of a 
search engine.  They store their data in a SQLITE3 database named
'spider.sqlite'.  This file can be removed at any time to restart the
process.   

You should install the SQLite browser to view and modify 
the databases from:

http://sqlitebrowser.org/

This program crawls a web site and pulls a series of pages into the
database, recording the links between pages.

Note: Windows has difficulty in displaying UTF-8 characters
in the console so for each console window you open, you may need
to type the following command before running this code:

    chcp 65001

http://stackoverflow.com/questions/388490/unicode-characters-in-windows-command-line-how

Mac: rm spider.sqlite
Mac: python3 spider.py

Win: del spider.sqlite
Win: spider.py

Enter web url: https://www.amazon.in/
Printing webs: ['https://www.amazon.in']
How many pages:2
1 https://www.amazon.in 222
66 https://www.amazon.in/b/ref=perc_essentials_desktop?node=21812268031 60
How many pages:

In this sample run, we told it to crawl a website and retrieve two 
pages.  If you restart the program again and tell it to crawl more
pages, it will not re-crawl any pages already in the database.  Upon 
restart it goes to a random non-crawled page and starts there.  So 
each successive run of spider.py is additive.

Mac: python3 spider.py 
Win: spider.py

Restarting existing crawl.  Remove spider.sqlite to start a fresh crawl.
Printing webs: ['https://www.amazon.in']
How many pages:10
370 https://www.amazon.in/l/16204586031?ref=cs_apay_t_mkyc_dk 60
341 https://www.amazon.in/gp/css/returns/homepage.html/ref=hp_gt_rt_ret 9
230 https://www.amazon.in/b/ref=HQPBISSDiwaliWave1?node=5866078031&pf_rd_p=1d462302-10f4-4719-9762-876dd153ccec&pf_rd_s=hero-quick-promo&pf_rd_t=201&pf_rd_i=B01A8B56ZE&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=GKGW1RCTR5W78BT5874W&pf_rd_r=GKGW1RCTR5W78BT5874W&pf_rd_p=1d462302-10f4-4719-9762-876dd153ccec 60
105 https://www.amazon.in/l/22771847031 60
465 https://www.amazon.in/-/ml/gp/sva/dashboard?ref_=nav_cs_apay Unable to retrieve or parse page
310 https://www.amazon.in/gp/help/customer/display.html?ref_=hp_left_v4_sib&nodeId=G202111950 98
253 https://www.amazon.in/product-reviews/B01A8B56ZE/ref=acr_dp_hist_3?ie=UTF8&filterByStar=three_star&reviewerType=all_reviews 155
241 https://www.amazon.in/Dynaflex-Amazon-Branded-Economy-Document/dp/B01A8B4SOE/ref=d_pb_allspark_dp_sims_pao_desktop_session_based_sccl_2_4/261-8798716-2083959?pd_rd_w=vdl7v&content-id=amzn1.sym.f9221308-d9c7-4a5c-ac35-a081ae29b064&pf_rd_p=f9221308-d9c7-4a5c-ac35-a081ae29b064&pf_rd_r=GKGW1RCTR5W78BT5874W&pd_rd_wg=j4SJT&pd_rd_r=0e3b0aae-ee70-49ca-ae04-83783b7f320b&pd_rd_i=B01A8B4SOE&psc=1 180
795 https://www.amazon.in/gp/profile/amzn1.account.AHJUEMIAJ6WGTGHDYHVR5I47FUUQ/ref=cm_cr_dp_d_gw_tr?ie=UTF8 60
612 https://www.amazon.in/-/ml/gp/help/customer/display.html?nodeId=201910090 88
How many pages:

You can have multiple starting points in the same database - 
within the program these are called "webs".   The spider
chooses randomly amongst all non-visited links across all
the webs.

If you want to dump the contents of the spider.sqlite file, you can 
run spdump.py as follows:

Mac: python3 spdump.py 
Win: spdump.py

(21, None, 1.0, 25, 'https://www.amazon.in/gcx/-/gfhz/?ref_=nav_cs_giftfinder')
(4, None, 1.0, 468, 'https://www.amazon.in/-/ml/computers-and-accessories/b/?ie=UTF8&node=976392031&ref_=nav_cs_pc')
(4, None, 1.0, 227, 'https://www.amazon.in/gp/help/customer/display.html/?ie=UTF8&nodeId=201149900')
(3, None, 1.0, 492, 'https://www.amazon.in/-/ml/gp/help/customer/display.html')
(3, None, 1.0, 218, 'https://www.amazon.in/gp/help/customer/display.html/ref=ddm_ft_dp?nodeId=200534000')
(3, None, 1.0, 196, 'https://www.amazon.in/gp/help/customer/display.html/ref=ap_cookie_error_help')
(2, None, 1.0, 795, 'https://www.amazon.in/gp/profile/amzn1.account.AHJUEMIAJ6WGTGHDYHVR5I47FUUQ/ref=cm_cr_dp_d_gw_tr?ie=UTF8')
(2, None, 1.0, 612, 'https://www.amazon.in/-/ml/gp/help/customer/display.html?nodeId=201910090')
(2, None, 1.0, 431, 'https://www.amazon.in/gp/help/customer/display.html?nodeId=GRK3YG3G4Y3R4LWJ&language=ml_IN')
(2, None, 1.0, 414, 'https://www.amazon.in/gp/help/customer/display.html?nodeId=202117440')
(2, None, 1.0, 409, 'https://www.amazon.in/gp/help/customer/display.html?nodeId=201633260')
(2, None, 1.0, 370, 'https://www.amazon.in/l/16204586031?ref=cs_apay_t_mkyc_dk')
(2, None, 1.0, 310, 'https://www.amazon.in/gp/help/customer/display.html?ref_=hp_left_v4_sib&nodeId=G202111950')
(2, None, 1.0, 253, 'https://www.amazon.in/product-reviews/B01A8B56ZE/ref=acr_dp_hist_3?ie=UTF8&filterByStar=three_star&reviewerType=all_reviews')
(2, None, 1.0, 241, 'https://www.amazon.in/Dynaflex-Amazon-Branded-Economy-Document/dp/B01A8B4SOE/ref=d_pb_allspark_dp_sims_pao_desktop_session_based_sccl_2_4/261-8798716-2083959?pd_rd_w=vdl7v&content-id=amzn1.sym.f9221308-d9c7-4a5c-ac35-a081ae29b064&pf_rd_p=f9221308-d9c7-4a5c-ac35-a081ae29b064&pf_rd_r=GKGW1RCTR5W78BT5874W&pd_rd_wg=j4SJT&pd_rd_r=0e3b0aae-ee70-49ca-ae04-83783b7f320b&pd_rd_i=B01A8B4SOE&psc=1')
(2, None, 1.0, 230, 'https://www.amazon.in/b/ref=HQPBISSDiwaliWave1?node=5866078031&pf_rd_p=1d462302-10f4-4719-9762-876dd153ccec&pf_rd_s=hero-quick-promo&pf_rd_t=201&pf_rd_i=B01A8B56ZE&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=GKGW1RCTR5W78BT5874W&pf_rd_r=GKGW1RCTR5W78BT5874W&pf_rd_p=1d462302-10f4-4719-9762-876dd153ccec')
(2, None, 1.0, 166, 'https://www.amazon.in/Sree-Ganesh-Sandal-Premium-Incense/dp/B09FM3MSDF/?_encoding=UTF8&pd_rd_w=VsKBg&content-id=amzn1.sym.a6b5fe4e-ef29-448b-8c4e-506bd7e10d9b&pf_rd_p=a6b5fe4e-ef29-448b-8c4e-506bd7e10d9b&pf_rd_r=1PEMFRJ3AGJZ989SD1TS&pd_rd_wg=i7S3H&pd_rd_r=3489df09-955d-434b-8b5c-c8fae86b318a&ref_=pd_gw_unk')
(2, None, 1.0, 105, 'https://www.amazon.in/l/22771847031')
(2, None, 1.0, 86, 'https://www.amazon.in/Dynaflex-Economy-Polybags-Document-16x14-inch/dp/B01A8B56ZE/?_encoding=UTF8&pd_rd_w=N0MKW&content-id=amzn1.sym.3c4cc815-e560-460b-a7fc-e14c8b8e9a29&pf_rd_p=3c4cc815-e560-460b-a7fc-e14c8b8e9a29&pf_rd_r=1PEMFRJ3AGJZ989SD1TS&pd_rd_wg=i7S3H&pd_rd_r=3489df09-955d-434b-8b5c-c8fae86b318a&ref_=pd_gw_trq_ed_cl4rs4co')
(2, None, 1.0, 66, 'https://www.amazon.in/b/ref=perc_essentials_desktop?node=21812268031')
(2, None, 1.0, 1, 'https://www.amazon.in')
(1, None, 1.0, 341, 'https://www.amazon.in/gp/css/returns/homepage.html/ref=hp_gt_rt_ret')
(1, None, 1.0, 263, 'https://www.amazon.in/hz/reviews-render/report-review?ie=UTF8&ref=cm_cr_dp_d_report&csrfT=hFNsUJAM2fza268NdsYvHnX8I1i3w9ATm7eXy0lsrkkbAAAAAGPBGVYAAAAB&reviewId=R2LI1IHIS14MQR')
(1, None, 1.0, 46, 'https://www.amazon.in/gp/redirect.html?_encoding=UTF8&location=https%3A%2F%2Fwww.amazon.in%2Fhfc%2Fbill%2Fcredit-cards%3Fref_%3Dgw_cc_finserv_ccbp&source=standards&token=6182DEC5F77BE4AACB845AE038CDD43A1FF0B369')
24 rows.

This shows the number of incoming links, the old page rank, the new page
rank, the id of the page, and the url of the page.  The spdump.py program
only shows pages that have at least one incoming link to them.

Once you have a few pages in the database, you can run Page Rank on the
pages using the sprank.py program.  You simply tell it how many Page
Rank iterations to run.

Mac: python3 sprank.py 
Win: sprank.py 

How many iterations:10
1 1.1119047619047613 
2 0.6855985449735447 
3 0.44683878180902054
4 0.29680271780780293
5 0.19898917097335708
6 0.13292080181048307
7 0.08918986717136783
8 0.05977085543307911
9 0.04009782813632001
10 0.02688838143545136
[(1, 0.5584475309318211), (25, 8.818132111978716), (46, 0.488779348009629), (66, 0.488779348009629), (86, 0.488779348009629)]

You can dump the database again to see that page rank has been updated:

Mac: python3 spdump.py 
Win: spdump.py 

(21, 8.818132111978716, 8.927067809034513, 25, 'https://www.amazon.in/gcx/-/gfhz/?ref_=nav_cs_giftfinder')
(4, 1.0415442436178743, 1.0402536874154045, 468, 'https://www.amazon.in/-/ml/computers-and-accessories/b/?ie=UTF8&node=976392031&ref_=nav_cs_pc')
(4, 0.8163485658336884, 0.8169817050082407, 227, 'https://www.amazon.in/gp/help/customer/display.html/?ie=UTF8&nodeId=201149900')
(3, 0.7827367263649812, 0.7801902655615534, 492, 'https://www.amazon.in/-/ml/gp/help/customer/display.html')
(3, 0.5785818676221209, 0.575252242667631, 218, 'https://www.amazon.in/gp/help/customer/display.html/ref=ddm_ft_dp?nodeId=200534000')
(3, 1.5621791007916699, 1.582164239514922, 196, 'https://www.amazon.in/gp/help/customer/display.html/ref=ap_cookie_error_help')
(2, 0.5106485252759588, 0.5061866819988854, 795, 'https://www.amazon.in/gp/profile/amzn1.account.AHJUEMIAJ6WGTGHDYHVR5I47FUUQ/ref=cm_cr_dp_d_gw_tr?ie=UTF8')
(2, 0.6563822061558355, 0.6511996553192103, 612, 'https://www.amazon.in/-/ml/gp/help/customer/display.html?nodeId=201910090')
(2, 0.6827226869921319, 0.6787623547991747, 431, 'https://www.amazon.in/gp/help/customer/display.html?nodeId=GRK3YG3G4Y3R4LWJ&language=ml_IN')
(2, 0.719949716269922, 0.7075690813683436, 414, 'https://www.amazon.in/gp/help/customer/display.html?nodeId=202117440')   
(2, 0.719949716269922, 0.7075690813683436, 409, 'https://www.amazon.in/gp/help/customer/display.html?nodeId=201633260')   
(2, 0.719949716269922, 0.7075690813683436, 370, 'https://www.amazon.in/l/16204586031?ref=cs_apay_t_mkyc_dk')
(2, 0.806548704310966, 0.7996270859694795, 310, 'https://www.amazon.in/gp/help/customer/display.html?ref_=hp_left_v4_sib&nodeId=G202111950')
(2, 0.4655080312491044, 0.46020179413410484, 253, 'https://www.amazon.in/product-reviews/B01A8B56ZE/ref=acr_dp_hist_3?ie=UTF8&filterByStar=three_star&reviewerType=all_reviews')       
(2, 0.4655080312491044, 0.46020179413410484, 241, 'https://www.amazon.in/Dynaflex-Amazon-Branded-Economy-Document/dp/B01A8B4SOE/ref=d_pb_allspark_dp_sims_pao_desktop_session_based_sccl_2_4/261-8798716-2083959?pd_rd_w=vdl7v&content-id=amzn1.sym.f9221308-d9c7-4a5c-ac35-a081ae29b064&pf_rd_p=f9221308-d9c7-4a5c-ac35-a081ae29b064&pf_rd_r=GKGW1RCTR5W78BT5874W&pd_rd_wg=j4SJT&pd_rd_r=0e3b0aae-ee70-49ca-ae04-83783b7f320b&pd_rd_i=B01A8B4SOE&psc=1')
(2, 0.4655080312491044, 0.46020179413410484, 230, 'https://www.amazon.in/b/ref=HQPBISSDiwaliWave1?node=5866078031&pf_rd_p=1d462302-10f4-4719-9762-876dd153ccec&pf_rd_s=hero-quick-promo&pf_rd_t=201&pf_rd_i=B01A8B56ZE&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=GKGW1RCTR5W78BT5874W&pf_rd_r=GKGW1RCTR5W78BT5874W&pf_rd_p=1d462302-10f4-4719-9762-876dd153ccec')
(2, 0.488779348009629, 0.4834589246812195, 166, 'https://www.amazon.in/Sree-Ganesh-Sandal-Premium-Incense/dp/B09FM3MSDF/?_encoding=UTF8&pd_rd_w=VsKBg&content-id=amzn1.sym.a6b5fe4e-ef29-448b-8c4e-506bd7e10d9b&pf_rd_p=a6b5fe4e-ef29-448b-8c4e-506bd7e10d9b&pf_rd_r=1PEMFRJ3AGJZ989SD1TS&pd_rd_wg=i7S3H&pd_rd_r=3489df09-955d-434b-8b5c-c8fae86b318a&ref_=pd_gw_unk')        
(2, 0.488779348009629, 0.4834589246812195, 105, 'https://www.amazon.in/l/22771847031')
(2, 0.488779348009629, 0.4834589246812195, 86, 'https://www.amazon.in/Dynaflex-Economy-Polybags-Document-16x14-inch/dp/B01A8B56ZE/?_encoding=UTF8&pd_rd_w=N0MKW&content-id=amzn1.sym.3c4cc815-e560-460b-a7fc-e14c8b8e9a29&pf_rd_p=3c4cc815-e560-460b-a7fc-e14c8b8e9a29&pf_rd_r=1PEMFRJ3AGJZ989SD1TS&pd_rd_wg=i7S3H&pd_rd_r=3489df09-955d-434b-8b5c-c8fae86b318a&ref_=pd_gw_trq_ed_cl4rs4co')
(2, 0.488779348009629, 0.4834589246812195, 66, 'https://www.amazon.in/b/ref=perc_essentials_desktop?node=21812268031')    
(2, 0.5584475309318211, 0.5539361472951618, 1, 'https://www.amazon.in')
(1, 0.719949716269922, 0.7075690813683436, 341, 'https://www.amazon.in/gp/css/returns/homepage.html/ref=hp_gt_rt_ret')    
(1, 0.4655080312491044, 0.46020179413410484, 263, 'https://www.amazon.in/hz/reviews-render/report-review?ie=UTF8&ref=cm_cr_dp_d_report&csrfT=hFNsUJAM2fza268NdsYvHnX8I1i3w9ATm7eXy0lsrkkbAAAAAGPBGVYAAAAB&reviewId=R2LI1IHIS14MQR')
(1, 0.488779348009629, 0.4834589246812195, 46, 'https://www.amazon.in/gp/redirect.html?_encoding=UTF8&location=https%3A%2F%2Fwww.amazon.in%2Fhfc%2Fbill%2Fcredit-cards%3Fref_%3Dgw_cc_finserv_ccbp&source=standards&token=6182DEC5F77BE4AACB845AE038CDD43A1FF0B369')
24 rows.

You can run sprank.py as many times as you like and it will simply refine
the page rank the more times you run it.  You can even run sprank.py a few times
and then go spider a few more pages sith spider.py and then run sprank.py
to converge the page ranks.

If you want to restart the Page Rank calculations without re-spidering the 
web pages, you can use spreset.py

Mac: python3 spreset.py 
Win: spreset.py 

All pages set to a rank of 1.0

Mac: python3 sprank.py 
Win: sprank.py 

How many iterations:100
1 0.018035994838875354
2 0.012096079624078245
3 0.00811315988493972
4 0.005441397759678289
5 0.0036495971628837387
....
97 6.245004513516506e-17
98 6.245004513516506e-17
99 1.850371707708594e-17
100 6.245004513516506e-17
[(1, 0.5539361472951618), (25, 8.927067809034513), (46, 0.4834589246812195), (66, 0.4834589246812195), (86, 0.4834589246812195)]

For each iteration of the page rank algorithm it prints the average
change per page of the page rank.   The network initially is quite 
unbalanced and so the individual page ranks are changing wildly.
But in a few short iterations, the page rank converges.  You 
should run prank.py long enough that the page ranks converge.

If you want to visualize the current top pages in terms of page rank,
run spjson.py to write the pages out in JSON format to be viewed in a
web browser.

Mac: python3 spjson.py 
Win: spjson.py 

Creating JSON output on spider_ain.js...
How many nodes? 20
Open force.html in a browser to view the visualization
 

You can view this data by opening the file force.html in your web browser.  
This shows an automatic layout of the nodes and links.  You can click and 
drag any node and you can also double click on a node to find the URL
that is represented by the node.

This visualization is provided using the force layout from:

http://mbostock.github.com/d3/

If you rerun the other utilities and then re-run spjson.py - you merely
have to press refresh in the browser to get the new data from spider.js.

