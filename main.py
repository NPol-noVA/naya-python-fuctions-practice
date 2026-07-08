{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a9c9482f-8688-4263-a80d-977942e868e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# a function for adding students' names and grades \n",
    "def add_student (name, grade): \n",
    "    students.append ({'names': name , 'grades': grade })\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e9ca2269-bb16-4768-89c4-05f28a523f63",
   "metadata": {},
   "outputs": [],
   "source": [
    "# function to calculate the average of grades\n",
    "def calculate_average (students):\n",
    "    c=0 ## counting students  \n",
    "    s=0 \n",
    "    for x in students: \n",
    "        s += float (x['grades'])\n",
    "        c=c+1\n",
    "    return float(s)/c "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1abf8c21-eb2d-49d3-a813-43d2c3f390db",
   "metadata": {},
   "outputs": [],
   "source": [
    "# function to look for a student then return its grade  \n",
    "def find_students ( students, name):\n",
    "    k= \" There's no student with this name\"  \n",
    "    for x in students: \n",
    "        if x['names']== name :\n",
    "            print ( name,\" is exsited and its grade is : \")\n",
    "            return x['grades']\n",
    "    return k "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6cf50964-6ce9-4872-a1fd-cb42dbd3deba",
   "metadata": {},
   "outputs": [],
   "source": [
    "#  function to print a report of students' information and highest  grade \n",
    "def display_report (students):\n",
    "    for x in students: \n",
    "        print ( x['names'],':' , x['grades']) \n",
    "\n",
    "    best_grade = 0 \n",
    "    for x in students: \n",
    "        if best_grade <= float(x['grades']):\n",
    "            best_grade = float(x['grades']) \n",
    "    print (\" Highest grade = \")  \n",
    "    return best_grade "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6821ca92-2b30-44b5-bd50-257a9962dc57",
   "metadata": {},
   "outputs": [],
   "source": [
    "# function tforo ask users   \n",
    "def option():\n",
    "    print(\" Okey will you choose new option (y/n) ?\") \n",
    "    response = input() \n",
    "    return response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3910f51e-5a57-4571-9de1-a9d7d4e2e879",
   "metadata": {},
   "outputs": [],
   "source": [
    "def list_options():\n",
    "     print (' This is the menu:',\n",
    "            \"1. add a student\",\"2. calculate average grade\", \"3. find a student's name\",\"4. show report\", \"5.exit\" ) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "80cb1850-1595-4a05-bd80-0c855df01319",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Have a nice week, this is a system to access student's grades  to show our menu enter y\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " This is the menu: 1. add a student 2. calculate average grade 3. find a student's name 4. show report 5.exit\n",
      " Enter your operation no: \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1\n",
      " Type a student name: (0 to stop) yarb\n",
      " Type a student grade:   100\n",
      " Type a student name: (0 to stop) noya\n",
      " Type a student grade:   88\n",
      " Type a student name: (0 to stop) paul\n",
      " Type a student grade:   70\n",
      " Type a student name: (0 to stop) jack\n",
      " Type a student grade:   90\n",
      " Type a student name: (0 to stop) 0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Okey will you choose new option (y/n) ?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Enter your operation no: \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "87.0\n",
      " Okey will you choose new option (y/n) ?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Enter your operation no: \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Type a student's same you want to find\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " laya\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " There's no student with this name\n",
      " Okey will you choose new option (y/n) ?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Enter your operation no: \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Type a student's same you want to find\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " jack\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "jack  is exsited and its grade is : \n",
      "90\n",
      " Okey will you choose new option (y/n) ?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Enter your operation no: \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yarb : 100\n",
      "noya : 88\n",
      "paul : 70\n",
      "jack : 90\n",
      " Highest grade = \n",
      "100.0\n",
      " Okey will you choose new option (y/n) ?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Enter your operation no: \n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Type a student's same you want to find\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " JACK \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " There's no student with this name\n",
      " Okey will you choose new option (y/n) ?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " n\n"
     ]
    }
   ],
   "source": [
    "print (\" Have a nice week, this is a system to access student's grades\", \" to show our menu enter y\")\n",
    "response = input() \n",
    "if response == 'y': \n",
    "    list_options() \n",
    "\n",
    "students = []\n",
    "while response == 'y':\n",
    "    print(\" Enter your operation no: \")\n",
    "    x = input()\n",
    "    \n",
    "    if x == '1':\n",
    "        while True:\n",
    "            name = input(\" Type a student name: (0 to stop)\")\n",
    "            if name == '0': \n",
    "                break\n",
    "                \n",
    "            grade = input(\" Type a student grade:  \")\n",
    "            add_student(name,grade)\n",
    "            \n",
    "        response = option()    \n",
    "        \n",
    "    elif x == '2': \n",
    "        print( calculate_average(students))\n",
    "        response = option()\n",
    "                \n",
    "    elif x == '3': \n",
    "        print(\" Type a student's same you want to find\") \n",
    "        ename = input() \n",
    "        print( find_students(students, ename))\n",
    "        response = option()\n",
    "            \n",
    "    elif x == '4': \n",
    "       print( display_report(students))\n",
    "       response = option() \n",
    "    elif x == '5':\n",
    "        print( \" EXIT!, THANKS FOR USING THIS SYSTEM \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30dbd3bf-cc90-4ace-ba53-3f930945c812",
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
   "version": "3.14.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
