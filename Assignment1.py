{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c9fbad60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.5117845117845118\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv(\"train.csv\")\n",
    "\n",
    "predictions = {}\n",
    "for passenger_index,passenger in df.iterrows():\n",
    "    passenger_id = passenger['PassengerId']\n",
    "    if passenger['Age'] < 40:\n",
    "        predictions[passenger_id] = 1\n",
    "    else:\n",
    "        predictions[passenger_id] = 0\n",
    "survived = df.Survived\n",
    "score = 0\n",
    "for i in range(len(predictions)):\n",
    "    if predictions[i+1]==survived[i]:\n",
    "        score+=1\n",
    "print(score/len(predictions))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "eacff080",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.6161616161616161\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv(\"train.csv\")\n",
    "\n",
    "predictions = {}\n",
    "for passenger_index,passenger in df.iterrows():\n",
    "    passenger_id = passenger['PassengerId']\n",
    "    if passenger['Sex'] == ['female']:\n",
    "        predictions[passenger_id] = 1\n",
    "    else:\n",
    "        predictions[passenger_id] = 0\n",
    "survived = df.Survived\n",
    "score = 0\n",
    "for i in range(len(predictions)):\n",
    "    if predictions[i+1]==survived[i]:\n",
    "        score+=1\n",
    "print(score/len(predictions))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13bdfefb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
