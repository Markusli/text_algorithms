# usage

# Default values
CONF="/wrk/protobios/scripts/spexWeb/spexs.json"
LIMIT=1000
METHOD="Counted" #Counted or Delimited
MINSEQS=4
MINMATCHES=4
PVALUE="1e-5"
RATIO=0
CHARS=3
NOSTARTINGGROUP="true"
SORTBY="+Hyper(fore,back)"
GENERATE="false"
REFERENCE="none"

# Command line parameters
if [ $# -eq 0 ] || [ $1 == "-h" ]
then
    echo "Usage: motifTree.sh [options]";
    echo $'\n'"Generates a motif tree from input peptides."$'\n'
    echo "Options:"
    echo "  -h"$'\t'$'\t'$'\t'"Show this help message and exit"
    echo "  -q QUERY"$'\t'$'\t'"Query peptides."
    echo "  -r REFERENCE"$'\t'"Reference peptides."
    echo "  -c CONF"$'\t'"Configuration file."  
    echo "  -o OUTFILE"$'\t'$'\t'"File for SPEXS output."
    echo "  -l LIMIT"$'\t'$'\t'"Maximum number of motifs in the output (default: 1000)."
    echo "  -m METHOD"$'\t'"Are counts provided (Counted) or not (Delimited) (default: Counted)."  
    echo "  -ms MINSEQS"$'\t'"Minimum number of unique sequences that motif has to match to in the query (default: 4)."  
    echo "  -mm MINMATCHES"$'\t'"Minimum number of sequences with duplicates that motif has to match to in the query (default: 4)."  
    echo "  -p PVALUE"$'\t'"Maximum p-value threshold for output motifs (default: 1e-5)."  
    echo "  -rat RATIO"$'\t'"Minimum ratio of Matches(fore, back) (default:0)."  
    echo "  -chr CHARS"$'\t'"Minimum number of characters a motif must contain, e.g. AHH and A.H.H both have 3 (default: 3)."  
    echo "  -n NOSTARTINGGROUP"$'\t'"If this is set to true, motif cannot start/end with dots (default: true)."  
    echo "  -s SORTBY"$'\t'"How to sort the output. +/- means biggest or smallest of some measure (default: -Hypher(fore, back))."  
    echo "  -g GENERATE"$'\t'"set to true when reference has to be generated (default: false)."
    exit 0
fi


while [ $# -gt 0 ]; do
    case $1 in
        -q) QUERY=$2 ; shift 2 ;;
        -r) REFERENCE=$2 ; shift 2 ;;
        -c) CONF=$2 ; shift 2 ;;        
        -o) OUTFILE=$2 ; shift 2 ;;
        -l) LIMIT=$2 ; shift 2 ;;
        -m) METHOD=$2 ; shift 2 ;;
        -ms) MINSEQS=$2 ; shift 2 ;;
        -mm) MINMATCHES=$2 ; shift 2 ;;
        -p) PVALUE=$2 ; shift 2 ;;
        -rat) RATIO=$2 ; shift 2 ;;
        -chr) CHARS=$2 ; shift 2 ;;
        -n) NOSTARTINGGROUP=$2 ; shift 2 ;;
        -s) SORTBY=$2 ; shift 2 ;;
        -g) GENERATE=$2 ; shift 2 ;;
        *) shift 1 ;;
    esac
done

# translating parameters into spexs format

if [ $REFERENCE == "none" ]
then
    REFERENCE=${QUERY}.generatedRef
fi

if [ $SORTBY == "pvalue" ]
then
    SORTBY="+Hyper(fore,back)"
fi

if [ $SORTBY == "ratio" ]
then
    SORTBY="+MatchesPropRatio(fore,back)"
fi

if [ $SORTBY == "seqs" ]
then
    SORTBY="+Seqs(fore)"
fi

if [ $SORTBY == "matches" ]
then
    SORTBY="+Matches(fore)"
fi

if [ $GENERATE == "false" ] && [ $METHOD == "Delimited" ]
then
    awk '{print "1" "\t" $1}' ${QUERY} > ${QUERY}.counts
    awk '{print "1" "\t" $1}' ${REFERENCE} > ${REFERENCE}.counts
    QUERY="${QUERY}.counts"
    REFERENCE="${REFERENCE}.counts"
fi

if [ $GENERATE == "true" ] && [ $METHOD == "Delimited" ]
then
    awk '{print "1" "\t" $1}' ${QUERY} > ${QUERY}.counts
    QUERY="${QUERY}.counts"
    /home/markus/Kool/Textalgorithms/projekt/generateReference.py -i ${QUERY} -o ${QUERY}.generatedRef
    REFERENCE="${QUERY}.generatedRef"    
fi

if [ $GENERATE == "true" ] && [ $METHOD == "Counted" ]
then
    /wrk/protobios/scripts/spexWeb/generateReference.py -i ${QUERY} -o ${QUERY}.generatedRef
    REFERENCE="${QUERY}.generatedRef"    
fi

# run spexs with the spexs.json file in the same folder as this script
/home/markus/go/src/github.com/egonelbre/spexs2/spexs2 -conf="${CONF}" inp="${QUERY}" ref="${REFERENCE}" limit="${LIMIT}" met="${METHOD}" ms="${MINSEQS}" mm="${MINMATCHES}" \
pval="${PVALUE}" rat="${RATIO}" chr="${CHARS}" nsg="${NOSTARTINGGROUP}" sb="${SORTBY}" > ${OUTFILE}
