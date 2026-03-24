# Cut 1 (initial solution)
# read n
# for ((i=0; i<$n; i++)); do
#     read
#     echo $REPLY | cut -c 3
# done


# CUT 1
# while read
# do
#     echo $REPLY | cut -c 3
# done


# CUT 2
# while read
# do
#     echo $REPLY | cut -c 2,7
# done


# CUT 3
# while read
# do
#     echo $REPLY | cut -c 2,3,4,5,6,7
# done


# CUT 4 
# while read; do
#     echo $REPLY | cut -c 1,2,3,4; done


# CUT 5
while read; do
    echo $REPLY | cut --output-delimiter="  "; done