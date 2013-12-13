'''
Created on Nov 9, 2013

@author: Bipin
'''
import random
import time
import string

from psych import psychapi
import yahooapi

allSentimentCsvFile = 'allnysesentiment.csv'
allNyseSymbols = ['DDD','MMM','WUBA','AHC','AIR','AAN','ABB','ABT','ABBV','ANF',
'SGF','ABM','AKR','ACN','ACMP','ACCO','AH','ACW','ACE','ATV',
'ACT','ATU','AYI','ADX','AGRO','PVD','ADT','AAP','AMD','ASX',
'AAV','ATE','AVK','AGC','LCM','ACM','ANW','AEB','AED','AEF',
'AEG','AEH','AEK','AEV','AER','ARX','ARO','AET','AFM','AMG',
'MGR','AFL','AFSD','MITT','MITT^A','MITT^B','AGCO','A','GAS','AEM',
'ADC','GRO','AGU','AL','APD','AYR','ARG','AKS','ALP^N','ALP^O',
'ALP^P','ALG','AGI','ALK','AIN','ALB','ALU','AA','ALR','ALR^B',
'ALEX','ALX','ARE','ARE^E','Y','ATI','AGN','ALE','AKP','ADS',
'AFB','AYN','AOI','AWF','ACG','AB','LNT','ATK','NCV','NCZ',
'NIE','NGZ','NFJ','AWH','ALSN','ALL','ALL^A','ALL^B','ALL^C','BSI',
'ALJ','ALDW','ANR','AGD','AWP','AOD','RESI','MO','AWC','ACH',
'AMBO','ACO','DOX','AEE','AMRC','AMX','AAT','AXL','ACC','AEO',
'AEP','AEL','AXP','AFA','AFG','AFQ','AFW','AMH','AMH^A','MRF',
'AIG','AIG/WS','AMID','XAA','ARL','ARPI','SLA','AWR','ASP','BSP',
'CSP','AMT','AVD','AWK','APU','AMP','AMP^A','ABC','ANFI','AHS',
'AP','APH','AMRE','AXR','AME','AFSI^A','APC','AU','BUD','AXE',
'ANN','NLY','NLY^A','NLY^C','NLY^D','BNNY','AR','ANH','ANH^A','ANH^B',
'AOL','AON','APA','AIV','AIV^Z','ARI','ARI^A','APO','AIB','AIY',
'AMTG','AMTG^A','AFT','AIF','AIT','ATR','WTR','ARSD','ABR','ABR^A',
'ABR^B','ARC','ARCX','MT','MTCN','ARH^C','ACI','ADM','ARCO','ASC',
'AFC','ARN','ARU','ARY','ACRE','ARDC','ARMF','AGX','AI','AIW',
'AHH','ARR','ARR^A','ARR^B','AWI','ARW','AJG','APAM','ASA','ABG',
'AHP$','AHT','AHT$','AHT^A','AHT^D','AHT^E','ASH','APB','GRR','AHL',
'AHL^A','AHL^B','AHL^C','ABW^B','AEC','AIZ','AGO','AGO^B','AGO^E','AGO^F',
'AF','AF^C','AZN','T','ATHL','AT','ATLS','APL','ARP','ATO',
'ATW','AUO','AUQ','ALV','AN','AZO','AVB','ACP','AVY','AVG',
'AVH','AVA','AVIV','AV','AVV','AVT','AVP','AVX','AXLL','AXS',
'AXS^C','AXS^D','AZZ','BGS','BWC','MCI','BGH','MPV','BMI','BHI',
'BBN','BLL','BYI','BALT','BGE^B','BBVA','BBD','BBDO','BCH','BLX',
'BSBR','BSAC','SAN','SAN^A','SAN^B','SAN^C','SAN^E','SAN^F','SAN^I','CIB',
'BXS','BAC','BAC/WS/A','BAC/WS/B','BAC^D','BAC^E','BAC^I','BAC^L','BAC^Z','BML^G',
'BML^H','BML^I','BML^J','BML^L','BOH','BMO','BK','BK^C','BNS','RATE',
'BKU','BCS','BCS^','BCS^A','BCS^C','BCS^D','BKS','B','CUDA','ABX',
'BAS','BAX','BTE','BBT','BBT^D','BBT^E','BBT^F','BBT^G','BFR','BBX',
'BCE','BEAM','TZF','BZH','BZT','BDX','BDC','BLC','BMS','BHE',
'BRK/A','BRK/B','BHLB','BRY','BBY','BGCA','BHP','BBL','BIG','BH',
'BBG','BIOA','BIOA/WS','BMR','BIO','BIO/B','BITA','BKH','BJZ','BFZ',
'CII','BHK','CYE','HYV','HYT','COY','BTZ','DSU','BHL','BQR',
'BGR','BDJ','EGF','FRA','BFO','BGT','BOE','BME','BHY','BAF',
'BNA','BKT','BGY','BKN','BTA','BIT','MUI','MNE','MUA','BPK',
'BKK','BIE','BBK','BBF','BYM','BFK','BTT','MEN','MUC','MUH',
'MHD','MFL','MUJ','MHN','MUE','MUS','MVT','MYC','MCA','MYD',
'MYF','MFT','MYM','MIY','MYJ','MJI','MYN','MPA','MQT','MYI',
'MQY','BNJ','BNY','BLH','BQH','BSE','BCF','BCX','BHD','BSD',
'BUI','BLK','BGB','BGX','BSL','BLT','BCRH','BXC','BTH','BWP',
'BA','BCC','BCEI','BAH','BWA','SAM','BXP','BXP^B','BSX','BTF',
'TEU','TEU^C','BYD','BP','BPT','BERY','BPZ','BRC','BDN^E','BDN',
'LND','BAK','BRE','BRE^D','BRFS','BPI','BGG','BFAM','EAT','BCO',
'BMY','BRS','BRX','BR','BKD','BAM','BOXC','DTLA^','INF','BIP',
'BOI','BPO','BPY','BEP','BRP','HTR','BRO','BF/A','BF/B','BWS',
'BRT','BC','BT','BPL','BKE','BVN','BBW','BG','BKW','BURL',
'CJES','BCR','GYB','PFH','CAB','CVC','CBT','COG','CACI','CAE',
'CAP','DVR','CCC','CWT','CALX','ELY','CPE','CPE^A','CPN','CBM',
'CPT','CCJ','CIS','CAM','CPB','CCG','CCG^A','CM','CNI','CNQ',
'CP','CAJ','CMN','COF^P','COF','COF/WS','CSU','BXMT','CSE','CMO',
'CMO^E','CRR','CAH','CFN','CSL','KMX','CCL','CUK','CRS','CSV',
'CRI','CSH','CAS','CAT','CATO','CBZ','CBL','CBL^D','CBL^E','CBO',
'IGR','CBG','CBS','CBS/A','CBX','CDI','CEC','FUN','CDR','CDR^B',
'CGI','CE','CLS','CEL','CPAC','CX','CNCO','CVE','CNC','CEN',
'CNP','EBR','EBR/B','CEE','CTL','CVO','CF','CGG','GIB','CSG',
'ECOM','CRL','CLDT','CKP','CHE','CHMT','CHMI','CHK','CHK^D','CHKR',
'CHSP','CHSP^A','CPK','CVX','CBI','CHS','CIM','CO','STV','DL',
'CEA','CHN','CGA','CHC','CHC/WS','LFC','MY','CHL','NPD','BORN',
'SNP','ZNH','CHA','CHU','XNY','CYD','ZX','CMG','CQB','CHH',
'CBK','CB','CHT','CHD','CBR','CI','HIS','XEC','CBB','CBB^B',
'CNK','CIR','CIT','BLW','C','C/WS/A','C/WS/B','C^C','C^E','C^J',
'C^K','C^N','C^P','C^Q','C^S','CTZ^A','CIA','CYN','CYN^C','CLC',
'CLH','CCO','CBA','CEM','EMO','CTR','CLW','CNL','CLF','CLV',
'CLX','CLD','MYCC','CMS','CMS^B','CNA','CNHI','CNO','CEO','COH',
'CIE','KOF','CCH','KO','CCE','CDE','CDE/WS','FOF','DVM','INB',
'UTF','LDP','MIE','RQI','RNP','PSF','RFI','CNS','COLE','CFX',
'CL','CXE','CMK','CIF','CXH','CMU','CLNY','CLNY^A','CXP','STK',
'CCV','CCZ','CMA','CMA/WS','FIX','CMC','CWH','CWH^D','CWH^E','CWHN',
'CWHO','CBU','CYH','CIG','CIG/C','CBD','ABV','ABV/C','SBS','ELP',
'CCU','CODI','CMP','CSC','CRK','CAG','CXO','CCM','COP','CNX',
'ED','CGX','STZ','STZ/B','CSTM','TCS','CLR','VLRS','CVG','CNW',
'COO','CTB','CPS','CPA','CLB','CLGX','CORR','COR','COR^A','GLW',
'BCA','GYC','OFC','OFC^H','OFC^L','CXW','CZZ','CMRE','CMRE^B','COT',
'COTY','CCSC','CFC^A','CFC^B','CUZ','CUZ^B','CVD','CVA','COV','CPF',
'CPL','ZY^A','CR','CRD/A','CRD/B','BAP','CS','CEQP','CRH','CRT',
'CCI','CCI^A','CCK','CRY','CSS','CST','CSX','CTS','CUBE','CUBE^A',
'CUB','CFR','CFR^A','CFI','CMI','CW','CSI','CVT','CVI','UAN',
'CVRR','CVS','CYNI','CYS','CYS^A','CYS^B','CYT','DHI','DAN','DHR',
'DAC','DQ','DRI','DAR','DVA','DPM','DCT','DDR','DDR^H','DDR^J',
'DDR^K','DF','DE','DEX','DDF','DKL','DK','DLPH','DAL','DEL',
'DLX','DMD','DWRE','DNR','HXM','DKT','DB','DTK','DTT','DUA',
'DXB','DCE','DVN','DV','DHT','DEO','DO','DRII','DRH','DSX',
'DHX','DKS','DBD','DLR','DLR^E','DLR^F','DLR^G','DGI','DDS','DDT',
'DIN','DFS','DFS^B','DNI','DM','DM^B','DLB','DG','DDC','DOM',
'D','DCUA','DCUB','DRU','DPZ','UFS','DCI','DRL','DSL','DBL',
'PLOW','DEI','DOV','DDE','DVD','DPD','DPO','DOW','DPS','RDY',
'DRD','DRC','DW','DHF','DMB','DSM','LEO','DRQ','DST','DSW',
'DTE','DTQ','DTZ','DCO','DPG','DNP','DTF','DUC','DUK','DUKH',
'DRE','DRE^J','DRE^K','DRE^L','DNB','DFT','DFT^A','DFT^B','DHG','DY',
'DYN','DYN/WS','DX','DX^A','DX^B','DD','DD^A','DD^B','SSP','EXP',
'EGP','EMN','KODK','ETN','ETV','ETW','EV','EOI','EOS','EFT',
'EFF','ETX','EOT','EVN','ETJ','EFR','EVF','EVG','EVT','ETO',
'EXD','ETG','ETB','ETY','EXG','ECT','ECL','DANG','EC','EDG',
'EIX','EDR','EW','EJ','EP^C','EE','EPB','ELN','EGO','LLY',
'ELLI','EFC','EARN','AKO/A','AKO/B','ERJ','EMC','EME','EMES','EBS',
'ESC','EMR','EDE','ESRT','EIG','EDN','EOC','ICA','ELX','EEQ',
'EEP','ENB','ECA','END','EXK','ENH','ENH^A','ENH^B','NDRO','EGN',
'ENR','ETE','ETP','ERF','ENI','ENS','EGL','E','EBF','NPO',
'ESV','ETM','EAA','EAB','EAE','ETR','ELA','ELB','ELJ','ELU',
'EFM','EMQ','EMZ','ENJ','EDT','EPD','EVC','ENV','EVHC','ENZ',
'EOG','EPAM','EPL','EPR','EPR^C','EPR^E','EPR^F','EQT','EQM','EQU',
'EFX','ELS','ELS^C','EQY','EQR','EQS','ERA','ESE','ESNT','ESS',
'ESS^H','EL','ESL','DEG','ETH','EEA','EVER','EVER^A','EVR','RE',
'EVTC','EXAM','EXAR','EXL','EXL^B','XCO','XLS','EXC','EXPR','EXH',
'EXR','XOM','FNB','FN','FDS','FICO','FDO','FFG','AGM','AGM/A',
'AGM^A','FRT','FSS','FTT','FII','FPT','FMN','FDX','FCH','FCH^A',
'FCH^C','FGP','FOE','FBR','FNF','FIS','FMO','FNP','FSCE','FAC',
'FAF','FBP','FBS^A','FCF','FHN','FHN^A','FR','AG','FMD','FNFG^B',
'FPO','FPO^A','FRC','FRC^A','FRC^B','FRC^C','FRC^D','FRC^E','FFA','FMY',
'FAV','FIF','FSD','FPF','FEI','FCT','FGB','FHY','FEO','FAM',
'FE','FMER^A','OAKS','FVE','FBC','DFP','PFD','PFO','FFC','FLC',
'FLT','FLTX','FTK','FLO','FLS','FLR','FLY','FMC','FTI','FMX',
'FL','F','FCE/A','FCE/B','FRX','FST','FOR','FDI','FRF','FIG',
'FSM','FBHS','FET','FNV','FC','BEN','FT','FI','FCX','FSL',
'FMS','FDP','FRO','FCN','FRM','FIO','FF','FXCM','GCV','GCV^B',
'GDV','GDV^A','GDV^D','GAB','GAB^D','GAB^G','GAB^H','GGT','GGT^B','GUT',
'GUT^A','GFA','GCAP','GBL','GNT','GME','GCI','GPS','IT','GLOG',
'GMT','GZT','GNK','GY','GNRC','GAM','GAM^B','BGC','GD','GEH',
'GEK','GE','GEB','GGP','GGP^A','GIS','GM','GM/WS/A','GM/WS/B','GM/WS/C',
'GM^B','GSI','GCO','GWR','GWRU','GEL','GNE','GNE^A','G','GPC',
'GNW','GEO','GPE^A','GGB','GTY','GFIG','GA','GIMO','GIL','GLT',
'GSK','GRT','GRT^G','GRT^H','GRT^I','BRSS','GCA','GGS','GHI','GLP',
'GPN','GSL','GMED','ALLY^A','ALLY^B','GKM','GOM','GNC','GOL','GFI',
'GG','GS','GS^A','GS^B','GS^C','GS^D','GS^I','GS^J','GSF','GSJ',
'TFG','GDP','GDP^C','GDP^D','GOV','IRE','GPX','GGG','GTI','GPT',
'GPT^A','GRAM','GVA','GRP/U','GPK','GTN','GTN/A','GNI','GXP','GXP^A',
'GXP^D','GXP^E','GB','GCH','GDOT','GBX','GHL','GEF','GEF/B','GFF',
'GPI','GMK','PAC','ASR','BSMX','TV','GSE','GSH','GES','GBAB',
'GGM','GPM','GGE','GEQ','GOF','GWRE','GUA','GLF','HQH','HQL',
'HRB','FUL','HAE','HK','HAL','HBI','HGR','HASI','HRG','HOG',
'HAR','HMY','HRS','HTSI','HSC','HHS','HGH','HIG','HIG/WS','HNR',
'HTS','HTS^A','HVT','HVT/A','HE','HE^U','HCA','HCC','HCI','HCJ',
'HCP','HDB','HW','HCN','HCN^I','HCN^J','HMA','HNT','HR','HTA',
'HLS','HPY','HL','HL^B','HEI','HEI/A','HAV','HIH','HHY','HMH',
'HSA','HLX','HP','HLF','HTGC','HTGY','HTGZ','HT','HT^B','HT^C',
'HSY','HTZ','HES','HPQ','HXL','HF','HGG','HCLP','ONE','HIW',
'HIL','HI','HRC','HSH','HTH','HNI','HEP','HFC','HD','HME',
'HMC','HON','HMN','HTF','HRL','HOS','HSP','HPT','HPT^D','HST',
'HSBC^B','HOV','HOVU','HHC','HBC','HBC^A','HCS','HCS^B','HBA^D','HBA^F',
'HBA^G','HBA^H','HBA^Z','HNP','HUB/A','HUB/B','HBM','HPP','HPP^B','HVB',
'HGT','HUM','HII','HUN','H','HDY','HY','IAG','IBN','IDA',
'IEX','IDT','CTC','IHS','ITW','IMN','IMAX','IFT','IMPV','IHC',
'IFN','IBA','CMLP','BLOX','INFY','IAE','IHD','IGA','IGD','IDG',
'IGK','IND','ING','INZ','ISF','ISG','ISP','IDE','IID','PPR',
'IRR','VOYA','IR','IM','INGR','IRC','IRC^A','IPHI','NSP','IEH',
'TEG','I','I^A','IHG','ICE','ICE$','IFF','IBM','IGT','IP',
'IRF','ISH','ISH^A','ISH^B','IOC','IPG','IPL^D','INXN','IL','IPI',
'XON','IVC','INVN','VBF','VCV','VTA','VLT','IVR','IVR^A','OIA',
'VMO','VKQ','VPV','IVZ','IQI','VVR','VTN','VGM','IIM','ITG',
'IRET','IRET^','IRET^B','IO','IRM','IRS','SZC','ISS','SFI','SFI^D',
'SFI^E','SFI^F','SFI^G','SFI^I','ITUB','ITC','ITT','ESI','IVH','JPM',
'JPM/WS','JPM^A','JPM^C','JPM^D','JCP','SJM','JBL','JEC','JHX','JNS',
'JEQ','JOF','JAH','JMI','JFC','JKS','JMP','JMPB','JBT','BTO',
'HEQ','JHS','JHI','HPF','HPI','HPS','PDT','HTD','HTY','JW/A',
'JW/B','JNJ','JCI','JONE','JNY','JLL','JRN','JOY','JNPR','JE',
'LRN','KAI','KAMN','KSU','KSU^','KS','KAR','KED','KYE','KMF',
'KYN','KYN^E','KYN^F','KYN^G','KB','KBH','KBR','KAP','KCG','K',
'KEM','KMPR','KMT','KW','KWN','KEG','KEY','KEY^G','KID','KRC',
'KRC^G','KRC^H','KMB','KIM','KIM^H','KIM^I','KIM^J','KIM^K','KMP','KMR',
'KMI','KMI/WS','KND','KFS','KGC','KEX','KRG','KRG^A','KKR','KFH',
'KFI','KFN','KFN^','KIO','KMG','KNX','KNL','KNOP','KOG','KSS',
'KNM','PHG','KOP','KEP','KEF','KF','KFY','KOS','KRA','KKD',
'KR','KRO','KT','KYO','LTD','SCX','LLL','LH','LG','LDR',
'LPI','LVS','LHO','LHO^G','LHO^H','LHO^I','LFL','LDF','LGI','LAZ',
'LOR','LZB','LDK','LF','LEA','LEE','BWG','LM','LEG','LGP',
'JZT','CVB','CWZ','HYL','JBJ','JBK','JBO','JZC','JZJ','JZK',
'JZL','JZV','KCC','KTH','KTN','KTP','XFP','XFR','XKE','XKO',
'XVG','JBI','LDOS','LPS','LEN','LEN/B','LII','LAS','LUK','LVLT',
'LXP','LXP^C','LXK','LPL','USA','ASG','LRY','LTM','LOCK','LITB',
'LIN','LNC','LNC/WS','LNN','LNKD','LGF','LAD','LYV','LYG','LYG^A',
'SCD','TLI','RIT','LMT','L','LO','LPX','LOW','LRE','LXU',
'LTC','LUB','LL','LXFR','LXFT','LUX','LDL','WLH','LYB','MTB',
'MTB/WS','MTB^','MTB^A','MTB^C','MDC','MHO','MHO^A','MAC','TUC','CLI',
'MGU','MIC','MFD','BMA','M','MCN','MSP','MMP','MGA','MX',
'MHR','MH^A','MHNA','MHNB','MAIN','MSCA','MMD','MNK','MZF','HYF',
'MANU','MTW','MN','MAN','MFC','MRO','MPC','MMI','MCS','MRIN',
'MPX','HZO','MKL','MWE','VAC','MMC','MSO','MLM','MAS','DOOR',
'MTZ','MA','MTDR','MTRN','MATX','MLP','MVNR','MXT','MMS','MXL',
'MBI','MNI','MKC','MKC/V','MDR','MCD','MUX','MHFI','MCK','MDU',
'MJN','MIG','MWV','MTL','MTL^','MEG','MPW','MED','MCC','MCQ',
'MCV','MD','MDT','MW','MRK','MCY','MDP','MTH','MTOR','MER^D',
'MER^E','MER^F','MER^K','MER^M','MER^P','PIY','PKH','PYY','PZB','MTR',
'MSB','MEI','MET','MET^A','MET^B','MLG','MLU','MTD','MXE','MXF',
'MFA','MFA^B','MFO','MIL','MCR','MGF','MIN','MMT','MFM','MFV',
'MTG','MGM','KORS','MAA','MEP','MSL','MPO','MM','MILL','MILL^C',
'MILL^D','MLR','MR','MSA','MTX','MP^D','MG','MTU','MIXT','MFG',
'MBT','MODN','MOD','MHK','MOH','TAP','TAP/A','MCP','MCP^A','MNR',
'MNR^A','MNR^B','MON','MWW','MTS','MRH','MRH^A','MCO','MOG/A','MOG/B',
'MS','MS^A','MS^E','MSJ','MSK','MSZ','MWG','MWO','MWR','APF',
'CAF','RNE','MSD','EDD','MSF','IIF','MOS','MSI','MOV','MPLX',
'MRC','ICB','HJN','HJV','HJJ','HJR','MSM','MSCI','MLI','MWA',
'MUR','MUSA','MVO','MVC','MVCB','MYE','NBR','NC','NTE','NBHC',
'NBG','NBG^A','NFG','NGG','NHI','NOV','NPK','NNN','NNN^D','NNN^E',
'SID','NSM','NW^C','NGS','NGVC','NRP','NTZ','NLS','NCI','NNA',
'NM','NMM','NAV','NAV^D','NCS','NCR','NP','NNI','NPTN','N',
'NSR','HYB','GF','IRL','NMFC','EDU','NRZ','NSLP','NWY','NYCB',
'NYCB^U','NYT','NCT','NCT^B','NCT^C','NCT^D','NWL','NFX','NJR','NEU',
'NEM','NR','NHF','NEE','NEE^C','NEE^F','NEE^G','NEE^H','NEE^I','NEE^J',
'NEE^O','NEE^P','NGL','NMK^B','NMK^C','NJ','NLSN','NKE','NTT','NKA',
'NI','NL','NED','NOAH','NE','NBL','NOK','NMR','NOR','NCFT',
'NAT','NDZ','JWN','NSC','NTL','NOA','NRT','NU','NTI','NOC',
'NRF','NRF^A','NRF^B','NRF^C','NRF^D','NWN','NWE','NVS','NVO','NQ',
'NRG','NYLD','DCM','NUS','NUE','NS','NSH','NSS','NEA^C','NUV',
'NUW','NAZ','NAZ^D','NBB','NBD','NAC','NQC','NCO','NCA','NCP',
'NCU^C','NUC','NVC','NTC','NTC^C','NTC^D','NTC^E','NTC^F','NTC^G','JCE',
'JQC','JGT','JDD','NAD','NAD^C','NZF^C','NVG^C','JMF','NEV','JLA',
'JPG','JPZ','JSN','JPW','JFR','JRO','NKG^C','NKG^D','JGG','JGV',
'NXC','NXN','NID','NQM','NMY','NMY^C','NMY^D','NMY^E','NMY^F','NMY^G',
'NMY^H','NGX^C','NMT','NMT^C','NMT^D','NUM','NOM^C','JLS','NMA','NMI',
'NMO','NIO','NUJ^C','NQJ','NNJ','NRK^C','NAN','NAN^C','NAN^D','NXK^C',
'NNY','NNP','NNC','NNC^C','NNC^D','NNC^E','NNC^F','NNC^G','NUO','NXM^C',
'NVY^C','NQP','NPY','NPP','JPI','JPC','NPF','NPM','NPT','NPI',
'NQU','NQI','JTP','JPS','JHP','JRI','NIM','NQS','NXP','NXQ',
'NXR','NSL','JSD','JTD','JTA','NTX','NTX^C','NPV','NIQ','JMT',
'NES','NVE','NVR','NYX','OAK','OAS','OXY','OII','OZM','OCIP',
'OCIR','OCN','ODP','OFG','OFG^A','OFG^B','OFG^D','OGE','OIBR','OIBR/C',
'OIS','ODC','OILT','ORI','OLN','OMG','OHI','OME','OCR','OCR^A',
'OCR^B','OMC','OMN','ASGN','OLP','OB','OKS','OKE','OPK','OPY',
'ORCL','ORAN','ORB','OWW','OEH','ORN','IX','ORA','OSK','OMI',
'OC','OI','OXM','OXF','PNG','PAI','ROYT','PACD','PCG','PKG',
'PLL','PANW','PAM','P','PHX','PAR','PKE','PKD','PH','PKY',
'PRE','PRE^D','PRE^E','PRE^F','PBF','BTU','PSO','PEB','PEB^A','PEB^B',
'PEB^C','PBA','PGH','PVA','PWE','PNTA','PEI','PEI^A','PEI^B','PFSI',
'PMT','PAG','PNR','PBY','POM','PEP','PKI','PBT','PRGO','PZE',
'PTR','PBR','PBR/A','PEO','PDH','PQ','PFE','PMC','PHH','PM',
'PHI','PSX','PSXP','PFX','PNX','FENG','DOC','PNY','PDM','PIR',
'PIKE','PCQ','PCK','PZC','PCM','PTY','PCN','PCI','PDI','PGP',
'PHK','PKO','PFL','PFN','PMF','PML','PMX','PNF','PNI','PYN',
'PNK','PF','PNW','PES','PHD','PHT','MAV','MHI','PXD','PSE',
'PJC','PBI','PBI^A','PBI^B','PAA','PAGP','PLT','PTP','PCL','PGEM',
'PNC','PNC/WS','PNC^P','PNC^Q','PNM','PII','POL','PPO','POR','PT',
'PKX','POST','PPS','PPS^A','POT','POWR','PPG','PPX','PPL','PPL^W',
'PYB','PYC','PYK','PYS','PYT','PYV','PX','PCP','PDS','PJA',
'PJL','PJS','PGI','PBH','PVG','PRI','PPP','PFG','PFG^B','PGZ',
'PVTD','PRA','PG','PGR','BIN','PLD','PRIS','PRIS/B','PRO','PRY',
'PB','PL','PL^B','PL^C','PL^E','PLP','PRLB','PFS','PFK','PJH',
'PRH','PRU','GHY','PUK','PUK^','PUK^A','ISD','PSB','PSB^R','PSB^S',
'PSB^T','PSB^U','PSB^V','TLK','PTGI','PEG','PSA','PSA^O','PSA^P','PSA^Q',
'PSA^R','PSA^S','PSA^T','PSA^U','PSA^V','PSA^W','PSA^X','PULS','PHA','PHM',
'PBYI','PCF','PMM','PIM','PMO','PPT','PVH','PVR','PZN','QEPM',
'QEP','QIHU','QRE','QTS','QUAD','KWR','NX','PWR','QTM','DGX',
'STR','KWK','ZQK','Q','CTQ','CTU','CTW','CTX','CTY','RAX',
'RDN','RSH','RAS','RAS^A','RAS^B','RAS^C','RALY','RL','RPT','RPT^D',
'RRC','RJD','RJF','RYN','RTN','RCS','RCAP','RMAX','RLD','RLGY',
'O','O^E','O^F','RHT','RLH','RLH^A','RWT','ENL','RUK','RBC',
'RGC','REG','REG^F','REG^G','RGP','RM','RF','RF^A','RGS','RGA',
'RZA','RS','RNR','RNR^C','RNR^E','SOL','RENN','RNF','RSG','RMD',
'REN','REN/WS','RFP','RSO','RSO^A','RSO^B','RH','RPAI','RPAI^A','REV',
'REX','REXR','RXN','RAI','RNO','RNG','RIOM','RIO','RBA','RAD',
'RLI','RLJ','RRTS','RHI','RKT','ROK','COL','ROC','RCI','ROG',
'ROL','ROP','RRMS','RST','RNDY','RSE','RDC','RY','RBS','RBS^E',
'RBS^F','RBS^G','RBS^H','RBS^I','RBS^L','RBS^M','RBS^N','RBS^P','RBS^Q','RBS^R',
'RBS^S','RBS^T','RCL','RDS/A','RDS/B','RGT','RMT','RVT','RES','RPM',
'RTI','RT','RKUS','R','RYL','RHP','SBR','SB','SB^B','SFE',
'SWY','CRM','SMM','SMF','SBH','SJT','SN','SD','SDT','SDR',
'PER','SNY','SOV^C','SAP','SAQ','SAR','SSL','BFS','BFS^A','BFS^C',
'SCG','SCU','SGK','SLB','SWM','SAIC','STNG','SMG','SNI','LBF',
'KHI','KMM','KTF','KST','KSM','SA','CKH','SDRL','SDLP','SEE',
'SSW','SSW^C','SSW^D','SEAS','JBN','JBR','SIR','SEM','SGZA','SEMG',
'SEMG/WS','SMI','SRE','ARK','SNH','SNHN','ST','SXT','SQNS','SCI',
'NOW','SSLT','SJR','SHW','SHG','SFL','SSTK','SBGL','SI','SIG',
'SBY','SSNI','SLW','SVM','AAZ^K','ZYZ^K','DDZ^K','FFZ^K','IIZ^K','SCR',
'SPG','SPG^J','SSD','SHI','SIX','SJW','SKM','SKX','SKH','SLG',
'SLG^I','SM','ZYY','ZYY^A','ZZA','ZZB','ZZD','ZZE','ZZF','ZZG',
'ZZH','ZZI','ZZJ','ZZJJ','SNN','AOS','SNA','SQM','SLRA','SWI',
'SLH','SAH','SON','SNE','BID','SFUN','SOR','SJI','SXE','SCE^F',
'SCE^G','SO','SCCO','LUV','SWX','SWN','SSS','CODE','SPA','SPE',
'SPE^','SE','SEP','SPB','TRK','SPR','SRC','SRLP','LEAF','S',
'SPW','JOE','STJ','STAG','STAG^A','STAG^B','SSI','SFG','SMP','SPF',
'SR','SXI','SWJ','SWK','SWU','STN','SGU','SRT','HOT','STWD',
'STT','STT^C','STO','SPLP','SCS','SCM','SCL','STE','STL','STL^A',
'STC','SF','SFB','SFN','SWC','STM','SGY','EDF','EDI','SGM',
'STON','SRI','STRI','SGL','BEE','BEE^A','BEE^B','BEE^C','SYK','RGR',
'SPH','SMFG','INN','INN^A','INN^B','INN^C','SMLP','SUI','SUI^A','SLF',
'SXCP','SXC','SU','SUNE','SXL','SHO','SHO^D','STP','STI','STI/WS/A',
'STI/WS/B','STI^A','STI^E','SPN','SUP','SVU','SUSS','SUSP','SFY','SWFT',
'SWZ','SWS','SYA','SMA','SYT','SNX','SNV','SNV^C','GJH','GJK',
'GJO','GJS','GJP','GJR','GJT','GJV','SYY','SYX','DATA','TAHO',
'TWN','TSM','XRS','TAL','TLM','TEP','TAM','SKT','TAOM','NGLS',
'TRGP','TGT','TARO','TTM','TCO','TCO^J','TCO^K','TMHC','TCP','TCB',
'TCB/WS','TCB^B','TCB^C','TSI','AMTD','TEL','TMH','TISI','TCK','TE',
'TK','TGP','TOO','TOO^A','TNK','TRC','TEO','TI','TI/A','TDY',
'TFX','VIV','TEF','TDA','TDE','TDI','TDJ','TDS','TU','TDF',
'EMF','TEI','GIM','TRF','TPX','TS','THC','TNC','TEN','TVC',
'TVE','TDC','TER','TEX','TX','TNH','TRNO','TRNO^A','TSO','TLLP',
'TTI','TEVA','TXI','TPL','TGH','TXT','TXTR','TTF','ACTV','AES',
'AES^C','BX','CSFS','SCHW','SCHW^B','CEB','SRV','SRF','DNY','GRX',
'GRX^A','GDL','GDL^B','THG','THGA','TRV','TMO','THR','TPRE','TSLF',
'TPGI','TC','TC^T','TRI','THO','TDW','TIF','TLYS','THI','TSU',
'TWC','TWX','TKR','TWI','TJX','TMUS','TOL','TR','TMK','TMK^B',
'TTC','TD','TYY','TYY^C','NDP','TYG','TYG^B','NTG','TYN','TTP',
'TPZ','TSS','TOT','TOWR','TW','TM','TAC','TAI','TRP','TCI',
'TDG','TLP','RIG','TGS','TA','TANN','TRR','TG','THS','TRMR',
'TREX','TY','TY^','TPH','TCAP','TCC','TCCA','TSL','TRN','GTS',
'TGI','TROX','TBI','TRLA','TRW','TNP','TNP^B','TNP^C','TUMI','TUP',
'TKC','TKF','TRQ','TPC','TWTR','TWO','TYC','TYL','TSN','USB',
'USB^A','USB^H','USB^M','USB^N','USB^O','USPH','SLCA','UBS','UBS^D','UCP',
'UGI','UIL','UPL','UGP','UMH','UMH^A','UA','UFI','UNF','UN',
'UL','UNP','UIS','UIS^A','UNT','UAL','UDR','UMC','UPS','URI',
'USM','UZA','X','UTX','UTX^A','UNH','UTL','UAM','UVV','UHT',
'UHS','UTI','UNS','UNM','URS','UBA','UBP','UBP^D','UBP^F','LCC',
'USAC','USNA','USU','USG','BIF','VFC','EGY','MTN','VCI','VALE',
'VALE/P','VRX','VLO','VHI','VR','VLY','VLY/WS','VMI','VAL','VNTV',
'VAR','VGR','VVC','VEEV','VTRB','VTR','VE','PAY','VZ','VET',
'VRS','VVI','VCO','VMEM','VIPS','VEL^E','VGI','DCA','V','VSH',
'VPG','VC','VSI','VMW','VOC','VCRA','VG','VNOD','VNO','VNO^G',
'VNO^I','VNO^J','VNO^K','VNO^L','VJET','VMC','WTI','WPC','WRB','WRB^B',
'GRA','GWW','WNC','WBC','WNA^/CL','WDR','WAGE','WAG','WD','WMT',
'DIS','WLT','WAC','WPO','WRE','WCN','WM','WAT','WSO','WSO/B',
'WTS','WPP','WCIC','WFT','WBS','WBS/WS','WBS^E','WTW','WRD','WRI',
'WRI^F','WMK','WCG','WLP','WFC','WFC/WS','WFC^J','WFC^L','WFC^N','WFC^O',
'WFC^P','WFC^Q','EOD','WAIR','WCC','WST','WR','WAL','WEA','ESD',
'EMD','GDO','EHI','GDF','HIX','HIO','HYI','IMF','IGI','MHY',
'MMU','WMC','DMO','MTT','MHF','MNP','GFY','SBW','WIW','WIA',
'WGP','WES','WNRL','WNR','WU','WAB','WLK','WBK','WHG','WEX',
'WY','WY^A','WGL','WHR','WTM','WSR','WWAV','WLL','WHX','WHZ',
'WG','WMB','WPZ','WSM','WSH','WGO','FUR','FUR^D','WRT','WIT',
'WEC','WNS','WWW','WF','WDAY','INT','WPT','WWE','WOR','WPX',
'WH','WX','WYN','XEL','XRM','XRX','XIN','XL','XOXO','XPO',
'XUE','XYL','AUY','YZC','YELP','YGE','YOKU','YPF','YUM','YUME',
'ZFC','ZLC','ZEP','ZMH','ZB^A','ZB^F','ZB^G','ZB^H','ZBK','ZTS',
'ZA','ZF','ZTR',]

samplePortfolio = {'AAPL': 200, 'IBM': 1000, 'A': 1200}

def createRandomPortfolio(portfolioSize=100, symbols=allNyseSymbols):
    randomPortfolio = dict()
    symbolCnt = len(symbols)
    for _ in range(portfolioSize):
        symbolIdx = random.randint(0, symbolCnt-1)
        symbol = symbols[symbolIdx]
        pos    = 100 * random.randint(1, 30)
        randomPortfolio[symbol] = pos
    return randomPortfolio    

def createNyseSentimentFile():
    f = open(allSentimentCsvFile, 'w')
    for i,symbol in enumerate(allNyseSymbols):
        s = ' %s,%s' % (symbol, psychapi.getSymbolMeanSentiment(symbol))
        print '(%d/%d) %s' % (i,len(allNyseSymbols),s)
        f.write('%s\n' % s)
        # if i > 20:
        #     break
    f.close()

def getAllNyseSymbols():
    f = open('nonzerosymbols.txt', 'r')
    symbols = [string.strip(x) for x in f if string.strip(x)]
    f.close()
    return symbols

def compareBuyAndHoldVsSimpleRebalance():
    symbols = getAllNyseSymbols()
    if symbols:
        allNyseSymbols = symbols
        
    prefix = 'Analyze Strategy Effectiveness - '

    startYear   = 2013
    startMonth  = 1
    day         = 8
    startPortfolio = createRandomPortfolio(portfolioSize=50, symbols=allNyseSymbols)
    
    print ' ******************************************************************** '
    print '       FinTech Hackathon 2013 Entry'
    print ' ******************************************************************** '
    print ' Personal Portfolio Rebalancer Based on Time Averaged Sentiment Indicators'
    print ' Current Positions in randomly generated portfolio: '
    print ' ******************************************************************** '

    print '\nPortfolio Composition:'
    for symbol in startPortfolio:
        print '\t\t %s: %d' % (symbol, startPortfolio[symbol])

    start_time = time.time()
    print '\tStrategy - Replace portfolio laggards monthly based on sentiment'
    portfolios = [startPortfolio] * 12
    dts        = ['2013-%02d-08' % x for x in range(1,12)]
    print '\tStrategy Analysis for dates - %s' % dts
    portfolio = startPortfolio
    for month in range(1,12):
        portfolios[month-1] = dict(portfolio)
        portfolioSentiments = psychapi.getSymbolMeanSentiments(portfolio.keys(), startYear, month, day=day)
        dt = '%d-%02d-%02d' % (startYear, month, day)
        print '\t%s: Recommended portfolio (using < 10%% turnover strategy):' % dt
        itemsToTrim = len(portfolio) / 10
        sellSymbols = set()
        buySymbols  = set()
        print '\t%s: Portfolio items to trim: %s' % (dt, itemsToTrim)
        if itemsToTrim > 0:
            lowestPortfolioSentiment = sorted(portfolioSentiments.values())[itemsToTrim-1]
            print '\t%s: Trim portfolio holding with sentiment at or below: %f' % (dt, lowestPortfolioSentiment)
        soldCnt = 0    
        for k,v in portfolioSentiments.items():
            if v <= lowestPortfolioSentiment:
                soldCnt += 1
                print '\t%s: Sell %s with one month average sentiment of %f' % (dt, k, v)
                sellSymbols.add(k)
        if soldCnt > 0:
            allCnt = len(portfolioSentiments)
            # print 'All NYSE symbol sentiment count %d' % allCnt
            highBullishCutoff = sorted(portfolioSentiments.values())[allCnt-soldCnt]
            buyCnt = 0
            for k,v in portfolioSentiments.items():
                if v >= highBullishCutoff:
                    buyCnt += 1
                    print '\t%s: Buy %s with one month average sentiment of %f' % (dt, k, v)
                    buySymbols.add(k)
                    if buyCnt >= soldCnt:
                        break
        portfolio = rebalancePortfolio(portfolio, sellSymbols, buySymbols, dts[month-1])

    end_time = time.time()
    # print '\t%s: Time to analyze %d stocks = %d seconds' %(dt, len(allNyseSymbols), end_time-start_time)
        
    print ' ******************************************************************** '
    print prefix
    yahooapi.printPortfolioValuationDifferences(portfolios, dts, 'Monthly Portfolio Rebalancing On Sentiment')
    yahooapi.printBuyAndHoldPortfolioValuation(startPortfolio, '2013-01-%02d' % day, '2013-11-%02d' % day)
    print ' ******************************************************************** '
    
def rebalancePortfolio(orig_portfolio, sellSymbols, buySymbols, valueDate):
    '''
    Starting with the portfolio, spend the same amount of money buying the buySymbols as the
    amount recovered from sellSymbols. The buy amounts are randomly generated, with the same range
    as the original random portfolio. And then scaled based on total amount
    '''
    sellPortfolio = {x:orig_portfolio[x] for x in sellSymbols}
    val1 = yahooapi.valuePortfolio(sellPortfolio, valueDate)
    buyPortfolio = {x:100 * random.randint(1, 30) for x in buySymbols}
    val2 = yahooapi.valuePortfolio(buyPortfolio, valueDate)
    if val2 < 0.00001:
        print 'Value of buy porttfolio %s is zero' % buyPortfolio
    else:
        scalingFactor = float(val1) / val2
        for symbol in buyPortfolio:
            qty = buyPortfolio[symbol] * scalingFactor
            buyPortfolio[symbol] = qty

    newPortfolio = dict(orig_portfolio)
    for x in sellSymbols:
        del newPortfolio[x]
    for x in buyPortfolio:
        if x in newPortfolio:
            qty = newPortfolio[x] + buyPortfolio[x]
        else:
            qty = buyPortfolio[x]
        newPortfolio[x] = qty
    return newPortfolio
    
def getAllNyseSentiments():        
    allNyseSentiments = dict()
    f = open(allSentimentCsvFile, 'r')
    for line in f:
        fields = string.strip(line).split(',')
        # print 'line=%s, fields=%s' % (line, fields)
        if len(fields) < 2:
            continue
        symbol = string.strip(fields[0])
        sentiment_str = string.strip(fields[1])
        if symbol and sentiment_str:
            try:
                sentiment = float(sentiment_str)
            except:
                print 'Cannot convert sentiment %s to float for symbol %s' % (sentiment_str, symbol)
            allNyseSentiments[symbol] = sentiment
    f.close()
    return allNyseSentiments

def Main():
    print ' ******************************************************************** '
    print ' FinTech Hackathon 2013 Entry'
    print ' ******************************************************************** '
    print ' Personal Portfolio Rebalancer Based on Time Averaged Sentiment Indicators'
    print ' Current Positions in randomly generated portfolio: '
    print ' ******************************************************************** '

    prefix = 'Strategy Execution - '
    symbols = getAllNyseSymbols()
    if symbols:
        allNyseSymbols = symbols

    allNyseSentiments = getAllNyseSentiments() 
    
    start_time = time.time()
    
    print prefix
    print '\tAnalyzing all %d stocks to determine top selection based on sentiment' % (len(allNyseSymbols))
    if False:
        createNyseSentimentFile()
    else:
        allNyseSentiments = getAllNyseSentiments()
    end_time = time.time()
    # print '\nTime to analyze %d stocks = %d seconds' %(len(allNyseSymbols), end_time-start_time)
        
    portfolioSize = 100
    portfolio = createRandomPortfolio(portfolioSize, symbols=allNyseSentiments.keys())    
    print '\nPortfolio Composition:'
    for symbol in portfolio:
        print '\t\t %s: %d' % (symbol, portfolio[symbol])

    print '\tMean Sentiments over the last month: (+ve = Bullish)'
    if True:
        portfolioSentiments = psychapi.getSymbolMeanSentiments(portfolio.keys(), 2013, 11, 10) 
        for symbol in sorted(portfolioSentiments.keys()):
            sentiment = portfolioSentiments[symbol]
            try:
                print '\t%s: %f' % (symbol, sentiment )
            except:
                print '\tError obtaining sentiment for symbol "%s"' % symbol
    else:
        portfolioSentiments = dict() 
        for symbol in portfolio:
            sentiment = psychapi.getSymbolMeanSentiment(symbol)
            portfolioSentiments[symbol] = sentiment
            print '\t %s: %f' % (symbol, sentiment )

    print prefix
    print '\tRecommended portfolio (using < 10% turnover strategy):'
    itemsToTrim = len(portfolio) / 10
    print '\tPortfolio items to trim: %s' % itemsToTrim
    
    if itemsToTrim > 0:
        lowestPortfolioSentiment = sorted(portfolioSentiments.values())[itemsToTrim-1]
        print '\tTrim portfolio holding with sentiment at or below: %f' % lowestPortfolioSentiment

    soldCnt = 0    
    for k,v in portfolioSentiments.items():
        if v <= lowestPortfolioSentiment:
            soldCnt += 1
            print '\tSell %s with one month average sentiment of %f' % (k, v)
        # else:
        #    print 'Retain %s with one month average sentiment of %f' % (k, v)
        
    # Buy as many as sold
    if soldCnt > 0:
        allCnt = len(allNyseSentiments)
        # print 'All NYSE symbol sentiment count %d' % allCnt
        highBullishCutoff = sorted(allNyseSentiments.values())[allCnt-soldCnt]
        buyCnt = 0
        for k,v in allNyseSentiments.items():
            if v >= highBullishCutoff:
                buyCnt += 1
                print '\tBuy %s with one month average sentiment of %f' % (k, v)
                if buyCnt >= soldCnt:
                    break
    
    print ''
    print ' ******************************************************************** '
    
    compareBuyAndHoldVsSimpleRebalance()
    
if __name__ == '__main__':
    Main()