source ~/.bashrc
mkdir /defects4j/TBarResult
python3 kinds.py | while read line
do
    bug_info=($line)
    defects4j checkout -p ${bug_info[0]} -v ${bug_info[1]}b -w /TBar/D4J/projects/${bug_info[0]}_${bug_info[1]}
    cd /TBar/D4J/projects/${bug_info[0]}_${bug_info[1]}
    defects4j compile
    defects4j fault-localization -w /TBar/D4J/projects/${bug_info[0]}_${bug_info[1]}
    python3 /defects4j/preprocess.py /TBar/D4J/projects/${bug_info[0]}_${bug_info[1]}/sfl/txt/line.ochiai.ranking.csv ${bug_info[0]}_${bug_info[1]}
    cd /TBar
  
   ./NormalFLTBarRunner.sh /TBar/D4J/projects/ ${bug_info[0]}_${bug_info[1]} /TBar/D4J/defects4j/ > /defects4j/TBarResult/${bug_info[0]}_${bug_info[1]}.txt
    #Follow part is test to this sh
    #bug_info=($line)
    #defects4j checkout -p Chart -v 8b -w /TBar/D4J/projects/Chart_8
    #cd /TBar/D4J/projects/Chart_8
    #defects4j compile
    #defects4j fault-localization -w /TBar/D4J/projects/Chart_8
    #python3 /defects4j/preprocess.py /TBar/D4J/projects/Chart_8/sfl/txt/line.ochiai.ranking.csv Chart_8
    #cd /TBar
    
    #./NormalFLTBarRunner.sh /TBar/D4J/projects/ Chart_8 /TBar/D4J/defects4j/ > /defects4j/TBarResult/Chart_8
    #break
done
