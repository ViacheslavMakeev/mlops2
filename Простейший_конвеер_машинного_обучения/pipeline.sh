is=$(( $RANDOM % 7 + 2 ))
for (( i=1; i <= is; i++ ))
do
echo $i "датасет:"
python3 data_creation.py
python3 model_preprocessing.py
python3 model_preparation.py
python3 model_testing.py
echo "- - - - - - - - - - - - - - "

done
