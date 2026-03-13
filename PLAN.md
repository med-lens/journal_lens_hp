googleスプレッドシートから、JSONで取得して、それをgithub pagesで表示したい。
ベースとなるHTMLは、Index.html
これはGASで表示するように使ってた。

スプレッドシートは、J_Medline_pseudoIF.csv　をアップロードしたもの。
gitignoreに入れるため、下に、一部を記載。3.5万行ある。
JrId,JournalTitle,MedAbbr,ISSN (Print),ISSN (Online),IsoAbbr,NlmId,SJR,SJR Best Quartile,H index,Citations / Doc. (2years),Total Docs. (2024),Total Docs. (3years),Total Citations (3years),Citable Docs. (3years),Categories,Areas,PseudoIF,MedIF
1,AADE editors' journal,AADE Ed J,0160-6999,,AADE Ed J,7708172,,,,,,,,,,,,
2,AANA journal,AANA J,0094-6354,2162-5239,AANA J,0431420,0.296,Q2,38.0,0.6,57.0,215.0,161.0,186.0,Advanced and Specialized Nursing (Q2); Medical and Surgical Nursing (Q2); Anesthesiology and Pain Medicine (Q3); Medicine (miscellaneous) (Q3),Medicine; Nursing,0.6,26.52
3,AARN news letter,AARN News Lett,0001-0197,,AARN News Lett,1251052,,,,,,,,,,,,
6,"Academy review of the California Academy of Periodontology, United States Section, ARPA Internationale",Acad Rev Calif Acad Periodontol,0008-0810,,Acad Rev Calif Acad Periodontol,7503275,,,,,,,,,,,,
9,Acquisitions medicales recentes,Acquis Med Recent,0075-4463,,Acquis Med Recent,0373054,,,,,,,,,,,,
11,Activitas nervosa superior,Act Nerv Super (Praha),0001-7604,,Act Nerv Super (Praha),0400662,,,,,,,,,,,,