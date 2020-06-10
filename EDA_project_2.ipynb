{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Task:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " You have been invited to participate in one of the UNICEF projects, an international UN entity whose mission is to increase the well-being of children around the world.\n",
    "The essence of the project is to track the impact of living conditions of students aged 15 to 22 on their academic performance in mathematics, in order to identify students at risk at an early stage.\n",
    "To do this, you need to build a model that would predict the results of the state exam in mathematics for each student in the school"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Attributes for  dataset:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "- school - student's school ('GP' or 'MS')\n",
    "- sex - student's sex ('F' - female or 'M' - male)\n",
    "- age - student's age (from 15 to 22)\n",
    "- address - student's home address type ('U' - urban or 'R' - rural)\n",
    "- famsize - family size ('LE3' - less or equal to 3 or 'GT3' - greater than 3)\n",
    "- Pstatus - parent's cohabitation status ('T' - living together or 'A' - apart)\n",
    "- Medu - mother's education (0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary   education or 4 – higher education)\n",
    "- Fedu - father's education (0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)\n",
    "- Mjob - mother's job ('teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')\n",
    "- Fjob - father's job ('teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')\n",
    "- reason - reason to choose this school (close to 'home', school 'reputation', 'course' preference or 'other')\n",
    "- guardian - student's guardian ('mother', 'father' or 'other')\n",
    "- traveltime - home to school travel time (1 - <15 min., 2 - 15-30 min., 3 - 30-60 min., 4 - >60 min.)\n",
    "- studytime - weekly study time (1 - <2 hours, 2 - 2-5 hours, 3 - 5-10 hours, 4 - >10 hours)\n",
    "- failures - number of past class failures (n if 1<=n<3, else 0)\n",
    "- schoolsup - extra educational support (yes or no)\n",
    "- famsup - family educational support (yes or no)\n",
    "- paid - extra paid classes (yes or no)\n",
    "- activities - extra-curricular activities (yes or no)\n",
    "- nursery - attended nursery school (yes or no)\n",
    "- higher - wants to take higher education (yes or no)\n",
    "- internet - Internet access at home (yes or no)\n",
    "- romantic - with a romantic relationship (yes or no)\n",
    "- famrel - quality of family relationships (from 1 - very bad to 5 - excellent)\n",
    "- freetime - free time after school (from 1 - very low to 5 - very high)\n",
    "- goout - going out with friends (from 1 - very low to 5 - very high)\n",
    "- health - current health status (from 1 - very bad to 5 - very good)\n",
    "- absences - number of school absences \n",
    "- score - gained score for the state exam"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Initial data review"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As the first step, we have to import some libraries and set the option to display more colums and rows then by default:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from itertools import combinations\n",
    "from scipy.stats import ttest_ind\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "pd.set_option('display.max_rows', 50)\n",
    "pd.set_option('display.max_columns', 50)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Let's open the dataset and look into it:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>school</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>address</th>\n",
       "      <th>famsize</th>\n",
       "      <th>Pstatus</th>\n",
       "      <th>Medu</th>\n",
       "      <th>Fedu</th>\n",
       "      <th>Mjob</th>\n",
       "      <th>Fjob</th>\n",
       "      <th>reason</th>\n",
       "      <th>guardian</th>\n",
       "      <th>traveltime</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>schoolsup</th>\n",
       "      <th>famsup</th>\n",
       "      <th>paid</th>\n",
       "      <th>activities</th>\n",
       "      <th>nursery</th>\n",
       "      <th>studytime, granular</th>\n",
       "      <th>higher</th>\n",
       "      <th>internet</th>\n",
       "      <th>romantic</th>\n",
       "      <th>famrel</th>\n",
       "      <th>freetime</th>\n",
       "      <th>goout</th>\n",
       "      <th>health</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>18</td>\n",
       "      <td>U</td>\n",
       "      <td>NaN</td>\n",
       "      <td>A</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>teacher</td>\n",
       "      <td>course</td>\n",
       "      <td>mother</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>17</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>other</td>\n",
       "      <td>course</td>\n",
       "      <td>father</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>LE3</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>health</td>\n",
       "      <td>NaN</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>-9.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>16</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>father</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>16</td>\n",
       "      <td>U</td>\n",
       "      <td>LE3</td>\n",
       "      <td>T</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>services</td>\n",
       "      <td>other</td>\n",
       "      <td>reputation</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>16</td>\n",
       "      <td>NaN</td>\n",
       "      <td>LE3</td>\n",
       "      <td>T</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>55.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>17</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>A</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>other</td>\n",
       "      <td>teacher</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>8</td>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>LE3</td>\n",
       "      <td>A</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>services</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>95.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>9</td>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  school sex  age address famsize Pstatus  Medu  Fedu      Mjob     Fjob  \\\n",
       "0     GP   F   18       U     NaN       A   4.0   4.0   at_home  teacher   \n",
       "1     GP   F   17       U     GT3     NaN   1.0   1.0   at_home    other   \n",
       "2     GP   F   15       U     LE3       T   1.0   1.0   at_home    other   \n",
       "3     GP   F   15       U     GT3       T   4.0   2.0    health      NaN   \n",
       "4     GP   F   16       U     GT3       T   3.0   3.0     other    other   \n",
       "5     GP   M   16       U     LE3       T   4.0   3.0  services    other   \n",
       "6     GP   M   16     NaN     LE3       T   2.0   2.0     other    other   \n",
       "7     GP   F   17       U     GT3       A   4.0   4.0     other  teacher   \n",
       "8     GP   M   15       U     LE3       A   3.0   2.0  services    other   \n",
       "9     GP   M   15       U     NaN     NaN   3.0   4.0     other    other   \n",
       "\n",
       "       reason guardian  traveltime  studytime  failures schoolsup famsup paid  \\\n",
       "0      course   mother         2.0        2.0       0.0       yes     no   no   \n",
       "1      course   father         1.0        2.0       0.0        no    yes   no   \n",
       "2       other   mother         1.0        2.0       3.0       yes     no  NaN   \n",
       "3        home   mother         1.0        3.0       0.0        no    yes  yes   \n",
       "4        home   father         1.0        2.0       0.0        no    yes  yes   \n",
       "5  reputation   mother         1.0        2.0       0.0        no    yes  yes   \n",
       "6        home   mother         1.0        2.0       0.0        no     no   no   \n",
       "7        home   mother         2.0        2.0       0.0       yes    yes   no   \n",
       "8        home   mother         1.0        2.0       0.0        no    yes  yes   \n",
       "9        home   mother         1.0        2.0       0.0        no    yes  yes   \n",
       "\n",
       "  activities nursery  studytime, granular higher internet romantic  famrel  \\\n",
       "0         no     yes                 -6.0    yes      NaN       no     4.0   \n",
       "1         no      no                 -6.0    yes      yes       no     5.0   \n",
       "2         no     yes                 -6.0    yes      yes      NaN     4.0   \n",
       "3        yes     yes                 -9.0    yes      yes      yes     3.0   \n",
       "4         no     yes                 -6.0    yes       no       no     4.0   \n",
       "5        yes     yes                 -6.0    yes      yes       no     5.0   \n",
       "6         no     yes                 -6.0    yes      yes       no     4.0   \n",
       "7         no     yes                 -6.0    yes       no       no     4.0   \n",
       "8         no     yes                 -6.0    yes      yes       no     NaN   \n",
       "9        yes     yes                 -6.0    yes      yes       no     5.0   \n",
       "\n",
       "   freetime  goout  health  absences  score  \n",
       "0       3.0    4.0     3.0       6.0   30.0  \n",
       "1       3.0    3.0     3.0       4.0   30.0  \n",
       "2       3.0    2.0     3.0      10.0   50.0  \n",
       "3       2.0    2.0     5.0       2.0   75.0  \n",
       "4       3.0    2.0     5.0       4.0   50.0  \n",
       "5       4.0    2.0     5.0      10.0   75.0  \n",
       "6       4.0    4.0     3.0       0.0   55.0  \n",
       "7       1.0    4.0     1.0       6.0   30.0  \n",
       "8       2.0    2.0     1.0       0.0   95.0  \n",
       "9       5.0    1.0     5.0       0.0   75.0  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_math = pd.read_csv('stud_math.csv')\n",
    "data_math.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 395 entries, 0 to 394\n",
      "Data columns (total 30 columns):\n",
      "school                 395 non-null object\n",
      "sex                    395 non-null object\n",
      "age                    395 non-null int64\n",
      "address                378 non-null object\n",
      "famsize                368 non-null object\n",
      "Pstatus                350 non-null object\n",
      "Medu                   392 non-null float64\n",
      "Fedu                   371 non-null float64\n",
      "Mjob                   376 non-null object\n",
      "Fjob                   359 non-null object\n",
      "reason                 378 non-null object\n",
      "guardian               364 non-null object\n",
      "traveltime             367 non-null float64\n",
      "studytime              388 non-null float64\n",
      "failures               373 non-null float64\n",
      "schoolsup              386 non-null object\n",
      "famsup                 356 non-null object\n",
      "paid                   355 non-null object\n",
      "activities             381 non-null object\n",
      "nursery                379 non-null object\n",
      "studytime, granular    388 non-null float64\n",
      "higher                 375 non-null object\n",
      "internet               361 non-null object\n",
      "romantic               364 non-null object\n",
      "famrel                 368 non-null float64\n",
      "freetime               384 non-null float64\n",
      "goout                  387 non-null float64\n",
      "health                 380 non-null float64\n",
      "absences               383 non-null float64\n",
      "score                  389 non-null float64\n",
      "dtypes: float64(12), int64(1), object(17)\n",
      "memory usage: 92.7+ KB\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>Medu</th>\n",
       "      <th>Fedu</th>\n",
       "      <th>traveltime</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>studytime, granular</th>\n",
       "      <th>famrel</th>\n",
       "      <th>freetime</th>\n",
       "      <th>goout</th>\n",
       "      <th>health</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>count</td>\n",
       "      <td>395.000000</td>\n",
       "      <td>392.000000</td>\n",
       "      <td>371.000000</td>\n",
       "      <td>367.000000</td>\n",
       "      <td>388.000000</td>\n",
       "      <td>373.000000</td>\n",
       "      <td>388.000000</td>\n",
       "      <td>368.000000</td>\n",
       "      <td>384.000000</td>\n",
       "      <td>387.000000</td>\n",
       "      <td>380.000000</td>\n",
       "      <td>383.000000</td>\n",
       "      <td>389.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>mean</td>\n",
       "      <td>16.696203</td>\n",
       "      <td>2.750000</td>\n",
       "      <td>2.614555</td>\n",
       "      <td>1.438692</td>\n",
       "      <td>2.038660</td>\n",
       "      <td>0.337802</td>\n",
       "      <td>-6.115979</td>\n",
       "      <td>3.937500</td>\n",
       "      <td>3.231771</td>\n",
       "      <td>3.105943</td>\n",
       "      <td>3.531579</td>\n",
       "      <td>7.279373</td>\n",
       "      <td>52.262211</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>std</td>\n",
       "      <td>1.276043</td>\n",
       "      <td>1.098127</td>\n",
       "      <td>2.228732</td>\n",
       "      <td>0.694181</td>\n",
       "      <td>0.842078</td>\n",
       "      <td>0.743135</td>\n",
       "      <td>2.526235</td>\n",
       "      <td>0.927277</td>\n",
       "      <td>0.993940</td>\n",
       "      <td>1.115896</td>\n",
       "      <td>1.396019</td>\n",
       "      <td>23.465197</td>\n",
       "      <td>22.919022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>min</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-12.000000</td>\n",
       "      <td>-1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>25%</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-6.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>40.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>50%</td>\n",
       "      <td>17.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-6.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>55.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>75%</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-3.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>70.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>max</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>-3.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>385.000000</td>\n",
       "      <td>100.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              age        Medu        Fedu  traveltime   studytime    failures  \\\n",
       "count  395.000000  392.000000  371.000000  367.000000  388.000000  373.000000   \n",
       "mean    16.696203    2.750000    2.614555    1.438692    2.038660    0.337802   \n",
       "std      1.276043    1.098127    2.228732    0.694181    0.842078    0.743135   \n",
       "min     15.000000    0.000000    0.000000    1.000000    1.000000    0.000000   \n",
       "25%     16.000000    2.000000    2.000000    1.000000    1.000000    0.000000   \n",
       "50%     17.000000    3.000000    2.000000    1.000000    2.000000    0.000000   \n",
       "75%     18.000000    4.000000    3.000000    2.000000    2.000000    0.000000   \n",
       "max     22.000000    4.000000   40.000000    4.000000    4.000000    3.000000   \n",
       "\n",
       "       studytime, granular      famrel    freetime       goout      health  \\\n",
       "count           388.000000  368.000000  384.000000  387.000000  380.000000   \n",
       "mean             -6.115979    3.937500    3.231771    3.105943    3.531579   \n",
       "std               2.526235    0.927277    0.993940    1.115896    1.396019   \n",
       "min             -12.000000   -1.000000    1.000000    1.000000    1.000000   \n",
       "25%              -6.000000    4.000000    3.000000    2.000000    3.000000   \n",
       "50%              -6.000000    4.000000    3.000000    3.000000    4.000000   \n",
       "75%              -3.000000    5.000000    4.000000    4.000000    5.000000   \n",
       "max              -3.000000    5.000000    5.000000    5.000000    5.000000   \n",
       "\n",
       "         absences       score  \n",
       "count  383.000000  389.000000  \n",
       "mean     7.279373   52.262211  \n",
       "std     23.465197   22.919022  \n",
       "min      0.000000    0.000000  \n",
       "25%      0.000000   40.000000  \n",
       "50%      4.000000   55.000000  \n",
       "75%      8.000000   70.000000  \n",
       "max    385.000000  100.000000  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_math.info()\n",
    "data_math.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "- **Numeric**: age, absences, score\n",
    "- **Nominal binary**: sex, address, famsize, Pstatus, schoolsup, famsup, paid, activities, nursery, higher, internet, romantic, school\n",
    "- **Nominal**: Medu, Fedu, Mjob, Fjob, reason, guardian, traveltime, studytime, failures, famrel, freetime, goout, health \n",
    "\n",
    "**Total columns** : 30 \n",
    "\n",
    "Column 'studytime, granular' - not described"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### I'm going to create some functions to make things more efficient:\n",
    "\n",
    "- to build plots \n",
    "- to calculate some essential stat indexes\n",
    "- to count missed values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_func(feature):\n",
    "\n",
    "    if data_math[feature].dtype == 'O':\n",
    "        sns.countplot(x=feature, data=data_math, label=feature)\n",
    "    else:\n",
    "        sns.distplot(a=data_math[feature], label=feature,\n",
    "                     kde=False, bins=data_math[feature].nunique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def stat_func(x):\n",
    "    Q1 = data_math[x].quantile(0.25)\n",
    "    Q2 = data_math[x].quantile(0.75)\n",
    "    IQR = Q2 - Q1\n",
    "    Missed_v = data_math[x].isnull().sum()\n",
    "    Unique_v = data_math[x].nunique()\n",
    "    disp = 'IQR: {} '.format(IQR), 'Outliers limit: [{f}, {l}] '.format(\n",
    "        f=Q1 - 1.5*IQR, l=Q2 + 1.5*IQR), 'Missed values: {} '.format(Missed_v), 'Unique values: {} '.format(Unique_v)\n",
    "\n",
    "    return disp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def missed_v(y):\n",
    "    missed = data_math[y].isnull().sum()\n",
    "\n",
    "    return ('Missed values: {} '.format(missed))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Now we can look into each column, let's start with age:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    395.000000\n",
       "mean      16.696203\n",
       "std        1.276043\n",
       "min       15.000000\n",
       "25%       16.000000\n",
       "50%       17.000000\n",
       "75%       18.000000\n",
       "max       22.000000\n",
       "Name: age, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 2.0 ',\n",
       " 'Outliers limit: [13.0, 21.0] ',\n",
       " 'Missed values: 0 ',\n",
       " 'Unique values: 8 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.age.describe())\n",
    "display(stat_func('age'))\n",
    "plot_func('age')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like a normal deviation and there are no missing values. \n",
    "Value \"22\" was considered as an outlier, but it's essential attribute so let's leave it"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### mother's education"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    392.000000\n",
       "mean       2.750000\n",
       "std        1.098127\n",
       "min        0.000000\n",
       "25%        2.000000\n",
       "50%        3.000000\n",
       "75%        4.000000\n",
       "max        4.000000\n",
       "Name: Medu, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 2.0 ',\n",
       " 'Outliers limit: [-1.0, 7.0] ',\n",
       " 'Missed values: 3 ',\n",
       " 'Unique values: 5 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.Medu.describe())\n",
    "display(stat_func('Medu'))\n",
    "plot_func('Medu')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Majority of mothers do not have higher education, \n",
    " but still almost all of them have attended school"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### father's education"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    371.000000\n",
       "mean       2.614555\n",
       "std        2.228732\n",
       "min        0.000000\n",
       "25%        2.000000\n",
       "50%        2.000000\n",
       "75%        3.000000\n",
       "max       40.000000\n",
       "Name: Fedu, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 1.0 ',\n",
       " 'Outliers limit: [0.5, 4.5] ',\n",
       " 'Missed values: 24 ',\n",
       " 'Unique values: 6 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.Fedu.describe())\n",
    "display(stat_func('Fedu'))\n",
    "plot_func('Fedu')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It seems that there is some error into the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.0     106\n",
       "3.0      96\n",
       "4.0      88\n",
       "1.0      78\n",
       "0.0       2\n",
       "40.0      1\n",
       "Name: Fedu, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_math.Fedu.value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Yes, there is just one wrong value as 40, looks like a typing mistake, let's replace it with 4:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_math.Fedu = data_math.Fedu.apply(lambda x: 4 if x == 40 else x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    371.000000\n",
       "mean       2.517520\n",
       "std        1.088808\n",
       "min        0.000000\n",
       "25%        2.000000\n",
       "50%        2.000000\n",
       "75%        3.000000\n",
       "max        4.000000\n",
       "Name: Fedu, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 1.0 ',\n",
       " 'Outliers limit: [0.5, 4.5] ',\n",
       " 'Missed values: 24 ',\n",
       " 'Unique values: 5 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.Fedu.describe())\n",
    "display(stat_func('Fedu'))\n",
    "plot_func('Fedu')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Almost all of the fathers have attended school, but majority doesn't have higher education"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### traveltime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    367.000000\n",
       "mean       1.438692\n",
       "std        0.694181\n",
       "min        1.000000\n",
       "25%        1.000000\n",
       "50%        1.000000\n",
       "75%        2.000000\n",
       "max        4.000000\n",
       "Name: traveltime, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 1.0 ',\n",
       " 'Outliers limit: [-0.5, 3.5] ',\n",
       " 'Missed values: 28 ',\n",
       " 'Unique values: 4 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.traveltime.describe())\n",
    "display(stat_func('traveltime'))\n",
    "plot_func('traveltime')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Majority of the students spend less then 30 min to reach school"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### studytime "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    388.000000\n",
       "mean       2.038660\n",
       "std        0.842078\n",
       "min        1.000000\n",
       "25%        1.000000\n",
       "50%        2.000000\n",
       "75%        2.000000\n",
       "max        4.000000\n",
       "Name: studytime, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 1.0 ',\n",
       " 'Outliers limit: [-0.5, 3.5] ',\n",
       " 'Missed values: 7 ',\n",
       " 'Unique values: 4 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.studytime.describe())\n",
    "display(stat_func('studytime'))\n",
    "plot_func('studytime')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Majority of the students spend less then 5 hours per week for extracurricular activities, which is not much"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### studytime, granular"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I\"m going to rename this column to studytime_gr as original title is not really suitable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    388.000000\n",
       "mean      -6.115979\n",
       "std        2.526235\n",
       "min      -12.000000\n",
       "25%       -6.000000\n",
       "50%       -6.000000\n",
       "75%       -3.000000\n",
       "max       -3.000000\n",
       "Name: studytime_gr, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 3.0 ',\n",
       " 'Outliers limit: [-10.5, 1.5] ',\n",
       " 'Missed values: 7 ',\n",
       " 'Unique values: 4 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAEHCAYAAABV4gY/AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAATXklEQVR4nO3df7BfdX3n8eerULFWrdhcLOWHFzTUgrbRXmO3lC4IKjpWpFtpomODZYy2sNXanS3YbrWdpbVWpJ3dqo2Fgq5AsMhKtypS6ujoVPCCEYhIBaQQk02u4rS6MnQS3v3je+7yJXxv7o/v9+abfPJ8zNy553zOj+87Z5JXzv3ccz6fVBWSpLb8wLgLkCSNnuEuSQ0y3CWpQYa7JDXIcJekBh087gIAVqxYUZOTk+MuQ5L2K7fccsu3qmpi0LZ5wz3JUcCHgB8DHgE2VNWfJ3k6sBGYBO4Dzqqq73THXACcA+wCfrOqrt/TZ0xOTjI9Pb3gP5AkCZL881zbFtItsxP47ar6SeBngXOTHA+cD9xYVSuBG7t1um1rgBOA04H3JTlouD+CJGkx5g33qtpWVbd2y98F7gSOAM4ALu92uxx4dbd8BnBVVT1cVd8A7gZWj7pwSdLcFvUL1SSTwPOBm4BnVNU26P0HABzW7XYE8EDfYVu6tt3PtT7JdJLpmZmZxVcuSZrTgsM9yZOBa4C3VtW/7mnXAW2PG+OgqjZU1VRVTU1MDPx9gCRpiRYU7kl+kF6wf6SqPtY1b09yeLf9cGBH174FOKrv8COBraMpV5K0EPOGe5IAlwB3VtV7+zZdB6zrltcBH+9rX5PkkCTHACuBm0dXsiRpPgt5zv1E4PXA7Uk2dW1vB94FXJ3kHOB+4DUAVbU5ydXAV+k9aXNuVe0aeeWSpDnNG+5V9XkG96MDnDrHMRcCFw5RlyRpCA4/IEkN2ieGH5D2ZVfcdP+4S9ivvPZFR4+7BOGduyQ1yXCXpAYZ7pLUIMNdkhpkuEtSgwx3SWqQ4S5JDTLcJalBhrskNchwl6QGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ0y3CWpQQuZIPvSJDuS3NHXtjHJpu7rvtm5VZNMJnmob9sHlrN4SdJgC5mJ6TLgfwIfmm2oql+ZXU5yEfAvffvfU1WrRlWgJGnxFjJB9ueSTA7aliTAWcCLR1uWJGkYw/a5nwRsr6qv97Udk+TLST6b5KS5DkyyPsl0kumZmZkhy5Ak9Rs23NcCV/atbwOOrqrnA28Drkjy1EEHVtWGqpqqqqmJiYkhy5Ak9VtyuCc5GPglYONsW1U9XFXf7pZvAe4Bjhu2SEnS4gxz534a8LWq2jLbkGQiyUHd8rHASuDe4UqUJC3WQh6FvBL4R+AnkmxJck63aQ2P7ZIB+AXgtiRfAf4GeHNVPTjKgiVJ81vI0zJr52g/e0DbNcA1w5clSRqGb6hKUoMMd0lqkOEuSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUIMNdkhpkuEtSgwx3SWrQQuZQvTTJjiR39LW9M8k3k2zqvl7Rt+2CJHcnuSvJy5arcEnS3BZy534ZcPqA9ouralX39QmAJMfTmzj7hO6Y9yU5aFTFSpIWZt5wr6rPAQ8u8HxnAFdV1cNV9Q3gbmD1EPVJkpZgmD7385Lc1nXbHNq1HQE80LfPlq7tcZKsTzKdZHpmZmaIMiRJu1tquL8feBawCtgGXNS1Z8C+NegEVbWhqqaqampiYmKJZUiSBllSuFfV9qraVVWPAB/k0a6XLcBRfbseCWwdrkRJ0mItKdyTHN63eiYw+yTNdcCaJIckOQZYCdw8XImSpMU6eL4dklwJnAysSLIFeAdwcpJV9Lpc7gPeBFBVm5NcDXwV2AmcW1W7lqd0SdJc5g33qlo7oPmSPex/IXDhMEVJkobjG6qS1CDDXZIaZLhLUoMMd0lqkOEuSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUoHnDPcmlSXYkuaOv7U+TfC3JbUmuTfK0rn0yyUNJNnVfH1jO4iVJgy3kzv0y4PTd2m4AnltVPwX8E3BB37Z7qmpV9/Xm0ZQpSVqMecO9qj4HPLhb26erame3+kXgyGWoTZK0RKPoc/814JN968ck+XKSzyY5aa6DkqxPMp1kemZmZgRlSJJmDRXuSX4X2Al8pGvaBhxdVc8H3gZckeSpg46tqg1VNVVVUxMTE8OUIUnazZLDPck64JXA66qqAKrq4ar6drd8C3APcNwoCpUkLdySwj3J6cDvAK+qqu/3tU8kOahbPhZYCdw7ikIlSQt38Hw7JLkSOBlYkWQL8A56T8ccAtyQBOCL3ZMxvwD8YZKdwC7gzVX14MATS5KWzbzhXlVrBzRfMse+1wDXDFuUJGk4vqEqSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUIMNdkhpkuEtSgwx3SWqQ4S5JDTLcJalBC5lD9VLglcCOqnpu1/Z0YCMwCdwHnFVV3+m2XQCcQ28O1d+squuXpXJJ+6Qrbrp/3CXsV177oqOX5bwLuXO/DDh9t7bzgRuraiVwY7dOkuOBNcAJ3THvS3LQyKqVJC3IvOFeVZ8DHtyt+Qzg8m75cuDVfe1XVdXDVfUN4G5g9YhqlSQt0FL73J9RVdsAuu+Hde1HAA/07bela3ucJOuTTCeZnpmZWWIZkqRBRv0L1Qxoq0E7VtWGqpqqqqmJiYkRlyFJB7alhvv2JIcDdN93dO1bgKP69jsS2Lr08iRJS7HUcL8OWNctrwM+3te+JskhSY4BVgI3D1eiJGmxFvIo5JXAycCKJFuAdwDvAq5Ocg5wP/AagKranORq4KvATuDcqtq1TLVLkuYwb7hX1do5Np06x/4XAhcOU5QkaTi+oSpJDTLcJalBhrskNchwl6QGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUHzTrM3lyQ/AWzsazoW+H3gacAbgZmu/e1V9YklVyhJWrQlh3tV3QWsAkhyEPBN4FrgDcDFVfWekVQoSVq0UXXLnArcU1X/PKLzSZKGMKpwXwNc2bd+XpLbklya5NBBByRZn2Q6yfTMzMygXSRJSzR0uCd5AvAq4KNd0/uBZ9HrstkGXDTouKraUFVTVTU1MTExbBmSpD6juHN/OXBrVW0HqKrtVbWrqh4BPgisHsFnSJIWYRThvpa+Lpkkh/dtOxO4YwSfIUlahCU/LQOQ5EnAS4A39TW/O8kqoID7dtsmSdoLhgr3qvo+8KO7tb1+qIokSUPzDVVJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUoKEehdT+6Yqb7h93CZKWmXfuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUIMNdkho07DR79wHfBXYBO6tqKsnTgY3AJL1p9s6qqu8MV6YkaTFGced+SlWtqqqpbv184MaqWgnc2K1Lkvai5eiWOQO4vFu+HHj1MnyGJGkPhg33Aj6d5JYk67u2Z1TVNoDu+2FDfoYkaZGGHfL3xKramuQw4IYkX1vogd1/BusBjj766CHLkCT1G+rOvaq2dt93ANcCq4HtSQ4H6L7vmOPYDVU1VVVTExMTw5QhSdrNksM9yQ8necrsMvBS4A7gOmBdt9s64OPDFilJWpxhumWeAVybZPY8V1TVp5J8Cbg6yTnA/cBrhi9TkrQYSw73qroX+OkB7d8GTh2mKEnScHxDVZIaZLhLUoMMd0lqkOEuSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGmS4S1KDDHdJapDhLkkNMtwlqUGGuyQ1yHCXpAYZ7pLUIMNdkhpkuEtSg4aZIPuoJJ9JcmeSzUne0rW/M8k3k2zqvl4xunIlSQsxzATZO4HfrqpbkzwFuCXJDd22i6vqPcOXtzBX3HT/3vooSdovDDNB9jZgW7f83SR3AkeMqjBJ0tKNpM89ySTwfOCmrum8JLcluTTJoXMcsz7JdJLpmZmZUZQhSeoMHe5JngxcA7y1qv4VeD/wLGAVvTv7iwYdV1UbqmqqqqYmJiaGLUOS1GeocE/yg/SC/SNV9TGAqtpeVbuq6hHgg8Dq4cuUJC3GME/LBLgEuLOq3tvXfnjfbmcCdyy9PEnSUgzztMyJwOuB25Ns6treDqxNsgoo4D7gTUNVKElatGGelvk8kAGbPrH0ciRJo+AbqpLUIMNdkhpkuEtSgwx3SWqQ4S5JDTLcJalBhrskNchwl6QGGe6S1CDDXZIaZLhLUoMMd0lqkOEuSQ0y3CWpQYa7JDXIcJekBhnuktQgw12SGrRs4Z7k9CR3Jbk7yfnL9TmSpMdblnBPchDwF8DLgePpTZp9/HJ8liTp8Zbrzn01cHdV3VtV/wZcBZyxTJ8lSdrNwct03iOAB/rWtwAv6t8hyXpgfbf6vSR3DfF5K4BvDXF8S7wWj+X1eJTX4rH2ievxuuEOf+ZcG5Yr3DOgrR6zUrUB2DCSD0umq2pqFOfa33ktHsvr8SivxWO1fj2Wq1tmC3BU3/qRwNZl+ixJ0m6WK9y/BKxMckySJwBrgOuW6bMkSbtZlm6ZqtqZ5DzgeuAg4NKq2rwcn9UZSfdOI7wWj+X1eJTX4rGavh6pqvn3kiTtV3xDVZIaZLhLUoP223BP8pokm5M8kmSqr/0lSW5Jcnv3/cXjrHNvmet6dNsu6IaBuCvJy8ZV47gkWZXki0k2JZlOsnrcNY1Tkv/c/V3YnOTd465nX5DkvySpJCvGXcuoLNdz7nvDHcAvAX+5W/u3gF+sqq1Jnkvvl7pH7O3ixmDg9eiGfVgDnAD8OPD3SY6rql17v8SxeTfwB1X1ySSv6NZPHm9J45HkFHpvi/9UVT2c5LBx1zRuSY4CXgLcP+5aRmm/vXOvqjur6nFvtVbVl6tq9pn6zcATkxyyd6vb++a6HvT+IV9VVQ9X1TeAu+kND3EgKeCp3fKPcGC/c/HrwLuq6mGAqtox5nr2BRcD/5XdXrTc3+234b5A/wn48uxf5APUoKEgDoSfZPq9FfjTJA8A7wEuGHM943QccFKSm5J8NskLx13QOCV5FfDNqvrKuGsZtX26WybJ3wM/NmDT71bVx+c59gTgT4CXLkdt47DE6zHvUBAt2NO1AU4FfquqrklyFnAJcNrerG9vmudaHAwcCvws8ELg6iTHVsPPRM9zPd5OQxnRb58O96pa0j/AJEcC1wK/WlX3jLaq8Vni9TgghoLY07VJ8iHgLd3qR4G/2itFjck81+LXgY91YX5zkkfoDaA1s7fq29vmuh5JngccA3wlCfT+bdyaZHVV/d+9WOKyaK5bJsnTgL8DLqiqL4y7nn3AdcCaJIckOQZYCdw85pr2tq3Af+yWXwx8fYy1jNv/pncNSHIc8AT2gZERx6Gqbq+qw6pqsqom6d0IvaCFYIf9ONyTnJlkC/AfgL9Lcn236Tzg2cB/6x5923QgPBEw1/Xohn24Gvgq8Cng3APsSRmANwIXJfkK8Ec8OtT0gehS4Ngkd9CbZ2Fdy10yBzKHH5CkBu23d+6SpLkZ7pLUIMNdkhpkuEtSgwx3SWqQ4S5JDTLctd9J8tYkT1rCcd+bZ/uqbtTI2fVXJTl/KTVK4+Zz7trvJLkPmKqqRb1ZmeR7VfXkPWw/uzvvecNVODpJDq6qneOuQ/uffXpsGSnJD9N7w/ZIepOtf5TeuPSfSfKtqjqlP7ST/DLwyqo6uxtu4Qp6f88/1XfODwN/MzvYWpKPABuBPwR+KMnPA38M/BBd2Ce5DHgIeA7wTOANwDp6bwTfVFVnd+d6KfAHwCHAPcAbqmrgTwzdTwnvpff6/63AsVX1yiTv7P6Mk9221w5zDXVgsltG+7rTga1V9dNV9Vzgz+iNFXNKVZ0yz7F/Dry/ql4I9I8X8lf0wpkkPwL8HPAJ4PeBjVW1qqo2DjjfofTGZfkt4G/pjQN+AvC8rktnBfB7wGlV9QJgGnjboMKSPJHexCovr6qfByZ22+VngDOqymDXkhju2tfdDpyW5E+SnFRV/7KIY08EruyWPzzbWFWfBZ7djTm0FrhmgV0ff9uNw3I7sL0beOoRepPCTNIbRvd44AtJNtG7s3/mHOd6DnBvN4EKfXXOuq6qHlpATdJAdston1ZV/5TkZ4BXAH+c5NODdutbfuIetvX7MPA6elMQ/toCy5md9OWRvuXZ9YOBXcANVbV2AecaNM5+v/+3wJqkgbxz1z4tyY8D36+q/0VvFqUXAN8FntK32/YkP5nkB4Az+9q/QC+8oRfk/S6jN0PT7MiZDDjvYn0RODHJs7van9QNqzvI1+iNzjjZrf/KEJ8rPY7hrn3d8+hNKrGJ3sw5/x3YAHwyyWe6fc4H/g/wD8C2vmPfApyb5Ev05k79/6pqO3An8Nd9zZ8Bju+GiV502FbVDHA2cGWS2+iF/XPm2Pch4DeATyX5PLAdWEyXk7RHPgqpA1L3nPzt9CZnGEuoJnlyVX0vvWmA/gL4elVdPI5a1B7v3HXASXIavW6R/zGuYO+8sfuJZDO9nyz+coy1qDHeuUvLLMm19Obq7Pc7VXX9oP2lUTDcJalBdstIUoMMd0lqkOEuSQ0y3CWpQf8OhXxjm/sovDoAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_math.rename(columns={'studytime, granular': 'studytime_gr'}, inplace=True)\n",
    "display(data_math.studytime_gr.describe())\n",
    "display(stat_func('studytime_gr'))\n",
    "plot_func('studytime_gr')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Looks like reversed distribution of studytime.\n",
    "Let's check what kind of correlation is between studytime and studytime_gr:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-0.9999999999999991"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_math['studytime'].corr(data_math['studytime_gr'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It's way too correlated, we don't need studytime_gr to be in our dataset, so i'm going to drop it\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_math.drop(['studytime_gr'], inplace=True, axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### failures "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    373.000000\n",
       "mean       0.337802\n",
       "std        0.743135\n",
       "min        0.000000\n",
       "25%        0.000000\n",
       "50%        0.000000\n",
       "75%        0.000000\n",
       "max        3.000000\n",
       "Name: failures, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 0.0 ',\n",
       " 'Outliers limit: [0.0, 0.0] ',\n",
       " 'Missed values: 22 ',\n",
       " 'Unique values: 4 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.failures.describe())\n",
    "display(stat_func('failures'))\n",
    "plot_func('failures')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It's good to know that most of the students didn't experience failures in personal matters"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### famrel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    368.000000\n",
       "mean       3.937500\n",
       "std        0.927277\n",
       "min       -1.000000\n",
       "25%        4.000000\n",
       "50%        4.000000\n",
       "75%        5.000000\n",
       "max        5.000000\n",
       "Name: famrel, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 1.0 ',\n",
       " 'Outliers limit: [2.5, 6.5] ',\n",
       " 'Missed values: 27 ',\n",
       " 'Unique values: 6 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.famrel.describe())\n",
    "display(stat_func('famrel'))\n",
    "plot_func('famrel')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I think there is a typing mistake, so i'm going to substitute this single negative value with the same but positive one:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    368.000000\n",
       "mean       3.942935\n",
       "std        0.903824\n",
       "min        1.000000\n",
       "25%        4.000000\n",
       "50%        4.000000\n",
       "75%        5.000000\n",
       "max        5.000000\n",
       "Name: famrel, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 1.0 ',\n",
       " 'Outliers limit: [2.5, 6.5] ',\n",
       " 'Missed values: 27 ',\n",
       " 'Unique values: 5 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_math.famrel = data_math.famrel.apply(lambda x: 1 if x == -1 else x)\n",
    "display(data_math.famrel.describe())\n",
    "display(stat_func('famrel'))\n",
    "plot_func('famrel')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It's nice that most of the students have good interpersonal relationships within the family"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### freetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    384.000000\n",
       "mean       3.231771\n",
       "std        0.993940\n",
       "min        1.000000\n",
       "25%        3.000000\n",
       "50%        3.000000\n",
       "75%        4.000000\n",
       "max        5.000000\n",
       "Name: freetime, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 1.0 ',\n",
       " 'Outliers limit: [1.5, 5.5] ',\n",
       " 'Missed values: 11 ',\n",
       " 'Unique values: 5 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.freetime.describe())\n",
    "display(stat_func('freetime'))\n",
    "plot_func('freetime')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Majority of the students have quite a lot of free time"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### goout"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    384.000000\n",
       "mean       3.231771\n",
       "std        0.993940\n",
       "min        1.000000\n",
       "25%        3.000000\n",
       "50%        3.000000\n",
       "75%        4.000000\n",
       "max        5.000000\n",
       "Name: freetime, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 2.0 ',\n",
       " 'Outliers limit: [-1.0, 7.0] ',\n",
       " 'Missed values: 8 ',\n",
       " 'Unique values: 5 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.freetime.describe())\n",
    "display(stat_func('goout'))\n",
    "plot_func('goout')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Looks like approx half of the students spend not much time going out, and another half vice versa"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### health"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    380.000000\n",
       "mean       3.531579\n",
       "std        1.396019\n",
       "min        1.000000\n",
       "25%        3.000000\n",
       "50%        4.000000\n",
       "75%        5.000000\n",
       "max        5.000000\n",
       "Name: health, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 2.0 ',\n",
       " 'Outliers limit: [0.0, 8.0] ',\n",
       " 'Missed values: 15 ',\n",
       " 'Unique values: 5 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.health.describe())\n",
    "display(stat_func('health'))\n",
    "plot_func('health')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Around 25% of students have health issues, that's quite a lot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### absences"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    383.000000\n",
       "mean       7.279373\n",
       "std       23.465197\n",
       "min        0.000000\n",
       "25%        0.000000\n",
       "50%        4.000000\n",
       "75%        8.000000\n",
       "max      385.000000\n",
       "Name: absences, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 8.0 ',\n",
       " 'Outliers limit: [-12.0, 20.0] ',\n",
       " 'Missed values: 12 ',\n",
       " 'Unique values: 36 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.absences.describe())\n",
    "display(stat_func('absences'))\n",
    "plot_func('absences')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see some values which are much greater then the rest, these are certanly the outliers, let's remove it:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    366.000000\n",
       "mean       4.603825\n",
       "std        4.965512\n",
       "min        0.000000\n",
       "25%        0.000000\n",
       "50%        4.000000\n",
       "75%        7.000000\n",
       "max       20.000000\n",
       "Name: absences, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 7.0 ',\n",
       " 'Outliers limit: [-10.5, 17.5] ',\n",
       " 'Missed values: 0 ',\n",
       " 'Unique values: 21 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_math = data_math.loc[data_math.absences <= 20]\n",
    "\n",
    "display(data_math.absences.describe())\n",
    "plot_func('absences')\n",
    "display(stat_func('absences'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now looks better, it's clearly seen that it's not popular to be abscent"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    366.000000\n",
       "mean       4.603825\n",
       "std        4.965512\n",
       "min        0.000000\n",
       "25%        0.000000\n",
       "50%        4.000000\n",
       "75%        7.000000\n",
       "max       20.000000\n",
       "Name: absences, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('IQR: 30.0 ',\n",
       " 'Outliers limit: [-5.0, 115.0] ',\n",
       " 'Missed values: 5 ',\n",
       " 'Unique values: 17 ')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.absences.describe())\n",
    "display(stat_func('score'))\n",
    "plot_func('score')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Seems that many people got 0 as score by unknown reasons, and the column with zeros stops the deviation from being normal, but i think we should leave zeros as it may be a real score for the exam."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Mjob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count       350\n",
       "unique        5\n",
       "top       other\n",
       "freq        123\n",
       "Name: Mjob, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 16 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.Mjob.describe())\n",
    "display(missed_v('Mjob'))\n",
    "plot_func('Mjob')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most women are working, which means they have some education for that"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Fjob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count       332\n",
       "unique        5\n",
       "top       other\n",
       "freq        185\n",
       "Name: Fjob, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 34 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.Fjob.describe())\n",
    "display(missed_v('Fjob'))\n",
    "plot_func('Fjob')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It seems that fathers prefer other types of job then healthcare and teaching, but they stay at home less then women"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### sex"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     366\n",
       "unique      2\n",
       "top         F\n",
       "freq      191\n",
       "Name: sex, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 0 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.sex.describe())\n",
    "display(missed_v('sex'))\n",
    "plot_func('sex')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Almost equal qty of boys and girls, but still there are a bit more girls\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### address"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     351\n",
       "unique      2\n",
       "top         U\n",
       "freq      273\n",
       "Name: address, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 15 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.address.describe())\n",
    "display(missed_v('address'))\n",
    "plot_func('address')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most of the students live in the city, which most probably means they spend less time to reach the school\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### famsize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     344\n",
       "unique      2\n",
       "top       GT3\n",
       "freq      245\n",
       "Name: famsize, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 22 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.famsize.describe())\n",
    "display(missed_v('famsize'))\n",
    "plot_func('famsize')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most of the students have more then 3 members in the family"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Pstatus"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     328\n",
       "unique      2\n",
       "top         T\n",
       "freq      296\n",
       "Name: Pstatus, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 38 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.Pstatus.describe())\n",
    "display(missed_v('Pstatus'))\n",
    "plot_func('Pstatus')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most of the parents stay together, which is good for kids"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### reason"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count        349\n",
       "unique         4\n",
       "top       course\n",
       "freq         129\n",
       "Name: reason, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 17 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.reason.describe())\n",
    "display(missed_v('reason'))\n",
    "plot_func('reason')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Leading reason is course, so some parents seem to want their kids to study"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### school"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     366\n",
       "unique      2\n",
       "top        GP\n",
       "freq      322\n",
       "Name: school, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 0 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.school.describe())\n",
    "display(missed_v('school'))\n",
    "plot_func('school')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "School GP is the most common into this dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### guardian"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count        336\n",
       "unique         3\n",
       "top       mother\n",
       "freq         229\n",
       "Name: guardian, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 30 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.guardian.describe())\n",
    "display(missed_v('guardian'))\n",
    "plot_func('guardian')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most of the students are guarded by mothers"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### schoolsup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     357\n",
       "unique      2\n",
       "top        no\n",
       "freq      310\n",
       "Name: schoolsup, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 9 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.schoolsup.describe())\n",
    "display(missed_v('schoolsup'))\n",
    "plot_func('schoolsup')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Seems the school do not really support majority of the students"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### famsup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     331\n",
       "unique      2\n",
       "top       yes\n",
       "freq      204\n",
       "Name: famsup, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 35 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.famsup.describe())\n",
    "display(missed_v('famsup'))\n",
    "plot_func('famsup')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Good that most of the families support their kids"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### paid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     328\n",
       "unique      2\n",
       "top        no\n",
       "freq      189\n",
       "Name: paid, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 38 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.paid.describe())\n",
    "display(missed_v('paid'))\n",
    "plot_func('paid')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "But still support doesn't mean to pay for extra math classes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### activities"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     352\n",
       "unique      2\n",
       "top       yes\n",
       "freq      184\n",
       "Name: activities, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 14 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.activities.describe())\n",
    "display(missed_v('activities'))\n",
    "plot_func('activities')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "More then a half of the students seem to be active with additional classes\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### nursery"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     350\n",
       "unique      2\n",
       "top       yes\n",
       "freq      277\n",
       "Name: nursery, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 16 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.nursery.describe())\n",
    "display(missed_v('nursery'))\n",
    "plot_func('nursery')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Majority of the students have attended nursery"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### higher"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     348\n",
       "unique      2\n",
       "top       yes\n",
       "freq      332\n",
       "Name: higher, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 18 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.higher.describe())\n",
    "display(missed_v('higher'))\n",
    "plot_func('higher')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most of the students want to get higher education"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### internet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     334\n",
       "unique      2\n",
       "top       yes\n",
       "freq      279\n",
       "Name: internet, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 32 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.internet.describe())\n",
    "display(missed_v('internet'))\n",
    "plot_func('internet')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most of the students have access to internet"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### romantic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     336\n",
       "unique      2\n",
       "top        no\n",
       "freq      225\n",
       "Name: romantic, dtype: object"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'Missed values: 30 '"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data_math.romantic.describe())\n",
    "display(missed_v('romantic'))\n",
    "plot_func('romantic')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Majority of the students don't have romantic relationships"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Correlation of the numeric attributes\n",
    "\n",
    "Just 3 columns are truly numeric, so let's look into the correlation between them"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>age</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.151493</td>\n",
       "      <td>-0.159306</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>absences</td>\n",
       "      <td>0.151493</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.081274</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>score</td>\n",
       "      <td>-0.159306</td>\n",
       "      <td>0.081274</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               age  absences     score\n",
       "age       1.000000  0.151493 -0.159306\n",
       "absences  0.151493  1.000000  0.081274\n",
       "score    -0.159306  0.081274  1.000000"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_math[['age', 'absences', 'score']].corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x648 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "nums = ['age', 'absences', 'score']\n",
    "plt.figure(figsize=(9, 9))\n",
    "sns.heatmap(data_math[nums].corr(), square=True,\n",
    "            fmt='.2f', linewidths=0.1, annot=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Negative correlation between age and score shows that elder students have lower score\n",
    "- Positive correlation between age and absences shows that younger students tend to skip classes more often\n",
    "- None of them are strongly correlated, so we should leave it as it is"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Boxplots for nominal attributes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_boxplot(column):\n",
    "    fig, ax = plt.subplots(figsize=(9, 3))\n",
    "    sns.boxplot(x=column, y='score',\n",
    "                data=data_math,\n",
    "                ax=ax)\n",
    "    plt.xticks(rotation=0)\n",
    "    ax.set_title('Boxplot for ' + column)\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiwAAADgCAYAAAAgwj0PAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAV8klEQVR4nO3de7SddX3n8ffHRCAIKJQQIVyiPbSKznghWpzeouDUekPXLBVGa6yuYcZlYzrtGkVwBscWii22sqLWpvWCClq0LqHKqBBQ6qqDHsApYrCcUYGEAAdR5BLBxO/8sZ/DbMJJckhy9vPLyfu1Vtbez28/l89O1lnnk9/z7GenqpAkSWrZY/oOIEmStD0WFkmS1DwLiyRJap6FRZIkNc/CIkmSmmdhkSRJzbOwSNolklSSsV20r0VJrkxyT5L37op97kCGdyX55Czs9w1Jvr6r9yvNdRYWaY5J8sMkG5Pcm+THSb6Y5Ii+c02Z4S/sU4A7gQOq6o9HEEtS4yws0tz0sqraDzgUuB1Y1XOeR+so4Lu1A3e2TDJ/FvJI6pmFRZrDqupnwGeBY6bGkjw+yceTTCa5Kck7kzwmyUFJ1iV5Wbfefkkmkry+W/5Ykg8lubQ7VfO1JEdNd9xtHOOpwIeA53UzQD+ZZtuPAcuBt3XrnJBk7yTvS3Jr9+d9Sfbu1l/W5X57ktuAj06zz7Eu791J7kzy90OvPa17T3cluT3JaUOb7tW9j3uSXJ9k6dB2T03y1SQ/6V57+fbe/4z+0SRNyx8gaQ5Lsi/wGuB/Dw2vAh4PPBn4beD1wO9X1V3AG4G/TXII8FfAt6vq40Pbvhb4E+Bg4NvA+Vs59NaOsRb4L8A3qmq/qnrClhtW1Ru6/f55t85lwOnAccAzgWcAzwXeObTZE4GDGMzMnDJNnj8BvgIcCBze5SPJ/sBlwJeAw4AxYM3Qdi8HPg08AbgYeH+33WOBf+z2eQiwAjg/ya9u6/1v5e9K0gxYWKS56fPd7MVPgRcCfwGQZB6DAvOOqrqnqn4IvBf4PYCq+grwGQa/tF8C/Oct9vvFqrqyqh5gUCKet+X1Mds7xg56LfDuqrqjqiaB/7nF/n4BnFFVD1TVxmm2/zmDMnNYVf2sqqauoXkpcFtVvbcbv6eqrhra7utVdUlVbQY+waAswaA87QecXVUPVtXlwBeAk2fp/Ut7PAuLNDe9opu92Bv4A+BrSZ7IYGZkL+CmoXVvAhYPLa8Gng58tKp+tMV+b5l6UlX3AncxmJkYNpNjPFqHTbO/4eNOdqe/tuZtQIBvdqdv3tiNHwH8321sd9vQ8/uBfbprZA4DbqmqX2yRaTGz8/6lPZ6FRZrDqmpzVX0O2Az8BoNP3kzNNkw5ElgPD82O/A3wceDN03xM+aHZlCT7MTgNc+sW62zzGMCOfEX8rdPsb/i429xnVd1WVf+pqg5jMGv0we693QL88g7mOWKL61Km3uP23r+kHWBhkeawDJzI4NqNtd2pjQuBM5Ps3100+0fA1P1Gpi44fSNwDvDxrsRMeXGS30iyF4PrQq6qqluGXmcGx7gdOLzbx0x9CnhnkoVJDgb+x9D+tivJq5Ic3i3+mEHB2czgNM4Tk/xhd2Hv/kl+bQa7vAq4j8GFwY9Nsgx4GfDpGbx/STvAwiLNTf+Y5F4G17CcCSyvquu711Yw+GX7feDrwAXAR5Icy+AX6+u7X7rvYfCL/dSh/V4AnMHgVNCxDK4tmc60x+heuxy4HrgtyZ0zfD9/CowD/wJcB1zTjc3Uc4Crur+Ti4GVVfWDqrqHwTU+L2Nw+udG4Pnb21lVPcjggtzfZTCj8kEGf283dKts6/1L2gHZgdscSNoDdR83XldV79zeupK0qznDIkmSmmdhkSRJzfOUkCRJap4zLJIkqXkWFkmS1Lzd+ltNDz744FqyZEnfMSRJ0i5y9dVX31lVC7cc360Ly5IlSxgfH+87hiRJ2kWS3DTduKeEJElS8ywskiSpebNWWJJ8JMkdSb4zNHZQkkuT3Ng9Hjj02juSTCT5XpLfma1ckiRp9zObMywfA160xdipwJqqOhpY0y2T5BjgJOBp3TYf3OIL1yRJ0h5s1i66raorkyzZYvhEYFn3/Dzgq8Dbu/FPV9UDwA+STADPBb4xW/n2NKtWrWJiYqLvGDtt/fr1ACxevLjnJDtvbGyMFStW9B1DknYLo76GZVFVbQDoHg/pxhcDw19Rv64be4QkpyQZTzI+OTk5q2HVno0bN7Jx48a+Y0iSRqyVjzVnmrFpvzOgqlYDqwGWLl3q9wrM0Fz5n/zKlSsBOPfcc3tOIkkapVHPsNye5FCA7vGObnwdcMTQeocDt444myRJatSoC8vFwPLu+XLgoqHxk5LsneRJwNHAN0ecTZIkNWrWTgkl+RSDC2wPTrIOOAM4G7gwyZuAm4FXAVTV9UkuBL4LbALeUlWbZyubJEnavczmp4RO3spLx29l/TOBM2crjyRJ2n15p1tJktS8Vj4lJEnaBbznUnu859KuYWGRJDXH+y1pSxYWSZpD5sr/5L3nkrbkNSySJKl5FhZJktQ8C4skSWqehUWSJDXPwiJJkppnYZEkSc2zsEiSpOZZWCRJUvMsLJIkqXkWFkmS1DwLiyRJap6FRZIkNc/CIkmSmmdhkSRJzbOwSJKk5llYJElS83opLEn+a5Lrk3wnyaeS7JPkoCSXJrmxezywj2ySJKk9Iy8sSRYDbwWWVtXTgXnAScCpwJqqOhpY0y1LkiT1dkpoPrAgyXxgX+BW4ETgvO7184BX9JRNkiQ1ZuSFparWA+cANwMbgLur6ivAoqra0K2zAThk1NkkSVKb+jgldCCD2ZQnAYcBj0vyukex/SlJxpOMT05OzlZMSZLUkD5OCZ0A/KCqJqvq58DngH8H3J7kUIDu8Y7pNq6q1VW1tKqWLly4cGShJUlSf/ooLDcDxyXZN0mA44G1wMXA8m6d5cBFPWSTJEkNmj/qA1bVVUk+C1wDbAKuBVYD+wEXJnkTg1LzqlFnkyRJbRp5YQGoqjOAM7YYfoDBbIskSdLDeKdbSZLUPAuLJElqnoVFkiQ1z8IiSZKaZ2GRJEnNs7BIkqTmWVgkSVLzLCySJKl5FhZJktS8Xu50u7tYtWoVExMTfcfQkKl/j5UrV/acRFPGxsZYsWJF3zEkzXEWlm2YmJjg299Zy+Z9D+o7ijqPebAAuPr7t/ecRADz7r+r7wiS9hAWlu3YvO9BbHzKi/uOITVpwQ2X9B1B0h7Ca1gkSVLzLCySJKl5FhZJktQ8C4skSWqeF91KEt7GoDXewqA9fd/CwMIiSQx+Qd54/bUcud/mvqMI2OvngxMAD9w03nMSAdx877y+I1hYJGnKkftt5rRn/7TvGFJzzrrmgL4jeA2LJElqn4VFkiQ1r5fCkuQJST6b5IYka5M8L8lBSS5NcmP3eGAf2SRJUnv6mmE5F/hSVT0FeAawFjgVWFNVRwNrumVJkqTRF5YkBwC/BXwYoKoerKqfACcC53WrnQe8YtTZJElSm/qYYXkyMAl8NMm1Sf4uyeOARVW1AaB7PGS6jZOckmQ8yfjk5OToUkuSpN70UVjmA88G/rqqngXcx6M4/VNVq6tqaVUtXbhw4WxllCRJDemjsKwD1lXVVd3yZxkUmNuTHArQPd7RQzZJktSgkReWqroNuCXJr3ZDxwPfBS4Glndjy4GLRp1NkiS1acZ3uk2yADiyqr63C467Ajg/yV7A94HfZ1CeLkzyJuBm4FW74DiSJGkOmFFhSfIy4BxgL+BJSZ4JvLuqXr4jB62qbwNLp3np+B3ZnyRJmttmekroXcBzgZ/AQ4VjyexEkiRJeriZnhLaVFV3J5nVMK1Zv3498+6/mwU3XNJ3FKlJ8+7/EevXb+o7hqQ9wEwLy3eS/EdgXpKjgbcC/zx7sSRJkv6/mRaWFcDpwAPABcCXgT+drVCtWLx4Mbc9MJ+NT3lx31GkJi244RIWL17UdwxJe4DtFpYk84CLq+oEBqVFkiRppLZ70W1VbQbuT/L4EeSRJEl6hJmeEvoZcF2SSxncSh+AqnrrrKSSJEkaMtPC8sXujyRJ0sjNqLBU1XndXWl/pRv6XlX9fPZiSdJorV+/nvvumcdZ1xzQdxSpOTfdM4/HrV/fa4aZ3ul2GXAe8EMgwBFJllfVlbMXTZIkaWCmp4TeC/z7qe8RSvIrwKeAY2crmCSN0uLFi3lg0wZOe/ZP+44iNeesaw5g78WLe80w01vzP3b4Sw+r6l+Bx85OJEmSpIeb6QzLeJIPA5/oll8LXD07kSRJkh5upoXlzcBbGNySP8CVwAdnK5QkSdKwmRaW+cC5VfWX8NDdb/eetVSSJElDZnoNyxpgwdDyAuCyXR9HkiTpkWZaWPapqnunFrrn+85OJEmSpIebaWG5L8mzpxaSLAU2zk4kSZKkh5vpNSwrgc8kuRUo4DDgNbOWSpIkachMC8uTgGcBRwKvBI5jUFwkac64+V5vzd+K2+8fnABYtO8vek4iGPxsHN1zhpkWlv9eVZ9J8gTghQzufPvXwK/NWjJJGqGxsbG+I2jIgxMTAOx9lP8uLTia/n9GZlpYNnePLwE+VFUXJXnXzhy4+2j0OLC+ql6a5CDg74ElDL6z6NVV9eOdOYYkzdSKFSv6jqAhK1euBODcc8/tOYlaMdOLbtcn+Rvg1cAlSfZ+FNtuzUpg7dDyqcCaqjqawceoT93J/UuSpDlipjMsrwZeBJxTVT9Jcijw33b0oEkOZzBbcybwR93wicCy7vl5wFeBt+/oMXaVefffxYIbLuk7hjqP+dngi+l+sY/XGbRg3v13AYv6jiFpDzCjwlJV9wOfG1reAGzYieO+D3gbsP/Q2KJuv1TVhiSHTLdhklOAUwCOPPLInYiwfX2fr9MjTUzcA8DYk/0l2YZF/pxIGomZzrDsMkleCtxRVVcnWfZot6+q1cBqgKVLl87qJ5U8p90ez2tL0p5p5IUF+HXg5UleDOwDHJDkk8DtSQ7tZlcOBe7oIZskSWrQzl44+6hV1Tuq6vCqWgKcBFxeVa8DLgaWd6stBy4adTZJktSmkReWbTgbeGGSGxnc6+XsnvNIkqRG9HFK6CFV9VUGnwaiqn4EHN9nHkmS1KaWZlgkSZKmZWGRJEnNs7BIkqTmWVgkSVLzLCySJKl5FhZJktQ8C4skSWqehUWSJDXPwiJJkppnYZEkSc2zsEiSpOZZWCRJUvMsLJIkqXkWFkmS1DwLiyRJat78vgNIknadVatWMTEx0XeMnTb1HlauXNlzkp03NjbGihUr+o6x27OwSJKas2DBgr4jqDEWFkmaQ/yfvOYqr2GRJEnNs7BIkqTmjbywJDkiyRVJ1ia5PsnKbvygJJcmubF7PHDU2SRJUpv6mGHZBPxxVT0VOA54S5JjgFOBNVV1NLCmW5YkSRp9YamqDVV1Tff8HmAtsBg4ETivW+084BWjziZJktrU6zUsSZYAzwKuAhZV1QYYlBrgkP6SSZKklvRWWJLsB/wD8IdV9dNHsd0pScaTjE9OTs5eQEmS1IxeCkuSxzIoK+dX1ee64duTHNq9fihwx3TbVtXqqlpaVUsXLlw4msCSJKlXfXxKKMCHgbVV9ZdDL10MLO+eLwcuGnU2SZLUpj7udPvrwO8B1yX5djd2GnA2cGGSNwE3A6/qIZskSWrQyAtLVX0dyFZePn6UWSRJ0u7BO91KkqTmWVgkSVLzLCySJKl5FhZJktQ8C4skSWqehUWSJDXPwiJJkppnYZEkSc2zsEiSpOZZWCRJUvMsLJIkqXkWFkmS1DwLiyRJap6FRZIkNc/CIkmSmmdhkSRJzbOwSJKk5llYJElS8ywskiSpeRYWSZLUPAuLJKk5l19+OcuWLeOKK67oO4oa0VxhSfKiJN9LMpHk1L7zSJJG76yzzgLgzDPP7DmJWtFUYUkyD/gA8LvAMcDJSY7pN5UkaZQuv/xyNm3aBMCmTZucZREAqaq+MzwkyfOAd1XV73TL7wCoqj+bbv2lS5fW+Pj4CBPuvlatWsXExETfMXba1HsYGxvrOcnOGxsbY8WKFX3HkJpzwgknPFRYAObPn89ll13WYyKNUpKrq2rpluNNzbAAi4FbhpbXdWMPSXJKkvEk45OTkyMNp/4tWLCABQsW9B1D0iwaLivTLWvPNL/vAFvINGMPmwKqqtXAahjMsIwi1Fzg/+Ql7S7mz5//iBkWqbUZlnXAEUPLhwO39pRFktSD00477WHLp59+ek9J1JLWCsu3gKOTPCnJXsBJwMU9Z5IkjdALXvCCh2ZV5s+fz/Of//yeE6kFTRWWqtoE/AHwZWAtcGFVXd9vKknSqE3Nsji7oilNfUro0fJTQpIkzS27y6eEJEmSHsHCIkmSmrdbnxJKMgnc1HcOjdzBwJ19h5A06/xZ3zMdVVULtxzcrQuL9kxJxqc7vylpbvFnXcM8JSRJkppnYZEkSc2zsGh3tLrvAJJGwp91PcRrWCRJUvOcYZEkSc2zsKhpSRYluSDJ95NcneQbSV6ZZFmSu5Ncm2RtkjP6zippxySpJJ8YWp6fZDLJF7rlRUm+kOT/JPlukkv6S6u+WFjUrCQBPg9cWVVPrqpjGXwh5uHdKv9UVc8ClgKvS3JsT1El7Zz7gKcnWdAtvxBYP/T6u4FLq+oZVXUMcOqoA6p/Fha17AXAg1X1oamBqrqpqlYNr1RV9wFXA7884nySdp3/Bbyke34y8Kmh1w4F1k0tVNW/jDCXGmFhUcueBlyzvZWS/BJwHOA3e0u7r08DJyXZB/i3wFVDr30A+HCSK5KcnuSwXhKqVxYW7TaSfKA7h/2tbug3k1wLfAU4u6osLNJuqps1WcJgduWSLV77MvBk4G+BpwDXJnnErds1t83vO4C0DdcD/2FqoarekuRgYLwb+qeqemkvySTNhouBc4BlwC8Nv1BVdwEXABd0F+P+FvAPow6o/jjDopZdDuyT5M1DY/v2FUbSrPsI8O6qum54MMkLkuzbPd+fwfVqN/eQTz1yhkXNqqpK8grgr5K8DZhk8GmCt/ebTNJsqKp1wLnTvHQs8P4kmxj8R/vvqupb06ynOcw73UqSpOZ5SkiSJDXPwiJJkppnYZEkSc2zsEiSpOZZWCRJUvMsLJKakuQNSd6/i/b1w+5mg5J2cxYWSZLUPAuLpJFI8rgkX+y+D+o7SV6T5DlJ/rkb+2Z3F1OAw5J8KcmNSf58aB8nJ7mu2/492xuXNHd4p1tJo/Ii4NaqeglAkscD1wKvqapvJTkA2Nit+0zgWcADwPeSrAI2A+9hcNfTHwNf6e6E/M3pxqvq86N7a5JmmzMskkblOuCEJO9J8pvAkcCGqVusV9VPq2pTt+6aqrq7qn4GfBc4CngO8NWqmuzWO5/BF+BtbVzSHGJhkTQSVfWvDGZBrgP+DHglsLXvBnlg6PlmBrPB2cq6WxuXNIdYWCSNRJLDgPur6pPAOcBxDK5VeU73+v5JtnWa+irgt5McnGQecDLwtW2MS5pDvIZF0qj8G+AvkvwC+DnwZgazI6uSLGBw/coJW9u4qjYkeQdwRbfdJVV1EcDWxiXNHX5bsyRJap6nhCRJUvMsLJIkqXkWFkmS1DwLiyRJap6FRZIkNc/CIkmSmmdhkSRJzbOwSJKk5v0/T/IKIfri+yYAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiwAAADgCAYAAAAgwj0PAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAVqUlEQVR4nO3df7BfdX3n8efLRCAhIkQCjRG42BtXXXdVvOPg6lqm2K0rWnRmbbH+SCs7TLs2Zrf1B1W60m5Q27HWTKatpkVBRRm0rtDq2NJYS91V14CMgkG5o4CEGC5QfkeE+N4/vufi5XqT3Py43/O5N8/HzJ3v95zv+fH6XuaS1/dzzvecVBWSJEkte1zfASRJkvbGwiJJkppnYZEkSc2zsEiSpOZZWCRJUvMsLJIkqXkWFkkHJEklGT1I2zo+yVVJ7kvypwdjm5IWBguLtEAkuSnJziT3J/nXJJ9LckLfuSYl+Y0kX97LYucAdwBHVdXvHaR97up+J/cmuTbJy/eyzkhXwhbvw35uSvKSA80rafcsLNLC8oqqWgasBHYAG3vOs69OAr5d+3FFyz0UjK90v5OjgQuBy5IsP4CMknpgYZEWoKr6EfBp4JmT85I8MclHk0wkuTnJeUkel2R5kluTvKJbblmS8SRv6KYvSvLBJFd2h2r+OclJM+13D/t4BvBB4AXdaMfdM6x7EbAGeFu3zEuSHJ7kA0lu634+kOTwbvnTutxvT/JD4CN7+Z38BPgwsAR4apLnJ9nSjbzsSPL+btGruse7uxwvSPLzSb6Y5M4kdyS5JMnRXY6PAScCf9st/7bJbNPe36OjMHvYt6TdsLBIC1CSpcCvAV+dMnsj8ETgqcAvAG8AfrOq7gLeCPxVkuOAPwOuraqPTln3tcD/Ao4FrgUu2c2ud7ePrcBv0Y12VNXR01esqt/otvsn3TL/CLwTOBV4DvBs4PnAeVNW+zlgOYORmXP28jtZDPxX4H7gRmADsKGqjgJ+HrisW/TF3ePRXY6vAAHeAzwZeAZwAnB+l/v1wC10o1tV9Sd7ytHZ3b4l7casj9FKmhc+m+QRYBlwO/DLAEkWMSgwz62q+4DJk1pfD1xYVf+Q5FPAZuBJwL+btt3PVdVV3bbeCdyT5ISq+sHkAnvbx36+n9cCa6vq9m4ffwh8CPiD7vWfAO+qqof2sI1TuxGdR4Bx4FVVdU+Sh4HRJMdW1R08ttw9RlWNd+sCTHQjIu/az/cEMOt9SxpwhEVaWF7ZjV4cDvwO8M9Jfo7ByMhhwM1Tlr0ZWDVlehPwLOAjVXXntO0+Wkyq6n7gLgajDVPNZh/76skzbG/qfie6w1978tWqOrqqjq2qU7uRG4CzgacBNyT5+p5Oxk1yXJJLk2xLci/wcQbvd3/Net+SBiws0gJUVbuq6jPALuBFDL558zCDQyeTTgS2waOjIx8CPgr89gxfU37020ZJljE4DHPbtGX2uA9gf24Nf9sM25u63/2+3XxV3VhVrwGOA/4Y+HSSI3ezzfd08/99dxjndQwOE+0uxwPA0smJ7ve7Yhb7lrQbFhZpAcrAmcAxwNaq2sXgPIkLkjyhO2n2dxmMFAC8o3t8I/A+4KPdP7KTXpbkRUkOY3Auy9emHg6CQUnayz52AE/ptjFbnwTOS7IiybHA/5yyvQOS5HVJVnQn406eBLwLmGBwqOmpUxZ/AoNzX+5Osgp467TN7Zi2/HeBI5KckeTxDM67OXwW+5a0GxYWaWH52yT3A/cCFwBrqur67rW1DD75fw/4MvAJ4MNJnsegWLyhKx1/zGDE4Nwp2/0Eg3M27gKex+DckpnMuI/utS8C1wM/THLHLN/PemAL8E3gW8A13byD4aXA9d3vawNwVlX9qKoeZPC7+z9J7k5yKvCHwCnAPcDngM9M29Z7GBSru5O8paruAf4b8NcMRpgeAKZ+a2jGfR+k9yUtSNmPyx1IOoR0Xze+tarO29uykjRXHGGRJEnNs7BIkqTmeUhIkiQ1zxEWSZLUPAuLJElq3ry+NP+xxx5bIyMjfceQJEkHydVXX31HVa2YPn9eF5aRkRG2bNnSdwxJknSQJLl5pvkeEpIkSc2zsEiSpObNWWFJ8uEktye5bsq85UmuTHJj93jMlNd+P8l4ku8k+eW5yiVJkuafuRxhuYjB/TKmOhfYXFWrgc3dNEmeCZwF/Ntunb+YduM1SZJ0CJuzk26r6qokI9Nmnwmc1j2/GPgS8PZu/qVV9RDw/STjwPOBr8xVPklaiDZu3Mj4+HjfMQ7Ytm3bAFi1alXPSQ7c6Ogoa9eu7TvGvDfsc1iOr6rtAN3jcd38VcDUW9Xf2s37GUnOSbIlyZaJiYk5DStJ6sfOnTvZuXNn3zHUkFa+1pwZ5s14z4Cq2gRsAhgbG/O+ApI0xUL5JL9u3ToANmzY0HMStWLYIyw7kqwE6B5v7+bfCpwwZbmnALcNOZskSWrUsAvLFcCa7vka4PIp889KcniSk4HVwP8bcjZJktSoOTsklOSTDE6wPTbJrcC7gPcClyU5G7gFeDVAVV2f5DLg28AjwJuqatdcZZMkSfPLXH5L6DW7een03Sx/AXDBXOWRJEnzl1e6lSRJzWvlW0KaY16boT1em0GSZs/ConnF6zJI0qHJwnKIWCif5L02gyQdmjyHRZIkNc/CIkmSmmdhkSRJzbOwSJKk5llYJElS8ywskiSpeRYWSZLUPAuLJElqnoVFkiQ1z8IiSZKaZ2GRJEnNs7BIkqTmWVgkSVLzLCySJKl5FhZJktQ8C4skSWpeL4Ulyf9Icn2S65J8MskRSZYnuTLJjd3jMX1kkyRJ7Rl6YUmyCngzMFZVzwIWAWcB5wKbq2o1sLmbliRJ6u2Q0GJgSZLFwFLgNuBM4OLu9YuBV/aUTZIkNWbohaWqtgHvA24BtgP3VNU/AMdX1fZume3AccPOJkmS2tTHIaFjGIymnAw8GTgyyev2Yf1zkmxJsmViYmKuYkqSpIb0cUjoJcD3q2qiqh4GPgP8B2BHkpUA3ePtM61cVZuqaqyqxlasWDG00JIkqT99FJZbgFOTLE0S4HRgK3AFsKZbZg1weQ/ZJElSgxYPe4dV9bUknwauAR4BvgFsApYBlyU5m0GpefWws0mSpDYNvbAAVNW7gHdNm/0Qg9EWSZKkx/BKt5IkqXkWFkmS1DwLiyRJap6FRZIkNc/CIkmSmmdhkSRJzbOwSJKk5vVyHZb5YuPGjYyPj/cdQ1NM/vdYt25dz0k0aXR0lLVr1/YdQ9ICZ2HZg/Hxca69biu7li7vO4o6j/txAXD193b0nEQAix68q+8Ikg4RFpa92LV0OTuf/rK+Y0hNWnLD5/uOIOkQ4TkskiSpeRYWSZLUPA8JSRKeZN8aT7BvT98n2FtYJInBP5A3Xv8NTly2q+8oAg57eHAA4KGbt/ScRAC33L+o7wgWFkmadOKyXbzjlHv7jiE1593XHNV3BM9hkSRJ7bOwSJKk5llYJElS8ywskiSpeRYWSZLUPAuLJElqXi+FJcnRST6d5IYkW5O8IMnyJFcmubF7PKaPbJIkqT19jbBsAL5QVU8Hng1sBc4FNlfVamBzNy1JkjT8wpLkKODFwIUAVfXjqrobOBO4uFvsYuCVw84mSZLa1McIy1OBCeAjSb6R5K+THAkcX1XbAbrH42ZaOck5SbYk2TIxMTG81JIkqTd9FJbFwCnAX1bVc4EH2IfDP1W1qarGqmpsxYoVc5VRkiQ1pI/Ccitwa1V9rZv+NIMCsyPJSoDu8fYeskmSpAYNvbBU1Q+BHyT5N92s04FvA1cAa7p5a4DLh51NkiS1adZ3a06yBDixqr5zEPa7FrgkyWHA94DfZFCeLktyNnAL8OqDsB9JkrQAzKqwJHkF8D7gMODkJM8B/qiqfmV/dlpV1wJjM7x0+v5sT5IkLWyzPSR0PvB84G54tHCMzE0kSZKkx5rtIaFHquqeJHMapjXbtm1j0YP3sOSGz/cdRWrSogfvZNu2R/qOcVBs27aNB+5bxLuvOarvKFJzbr5vEUdu29ZrhtkWluuS/DqwKMlq4M3A/527WJIkST8128KyFngn8BDwCeDvgfVzFaoVq1at4ocPLWbn01/WdxSpSUtu+DyrVh3fd4yDYtWqVTz0yHbeccq9fUeRmvPua47i8FWres2w18KSZBFwRVW9hEFpkSRJGqq9nnRbVbuAB5M8cQh5JEmSfsZsDwn9CPhWkisZXEofgKp685ykkiRJmmK2heVz3Y8kSdLQzaqwVNXF3VVpn9bN+k5VPTx3sSRJkn5qtle6PQ24GLgJCHBCkjVVddXcRZMkSRqY7SGhPwX+0+R9hJI8Dfgk8Ly5CtaKRQ/e5YXjGvK4Hw2+cvqTI7y4VwsWPXgXsDC+1iypbbMtLI+fetPDqvpuksfPUaZmjI6O9h1B04yP3wfA6FP9R7INx/t3ImkoZltYtiS5EPhYN/1a4Oq5idSOtWvX9h1B06xbtw6ADRs29JxEkjRMsy0svw28icEl+QNcBfzFXIWSJEmaaraFZTGwoareD49e/fbwOUslSZI0xV6vdNvZDCyZMr0E+MeDH0eSJOlnzbawHFFV909OdM+Xzk0kSZKkx5ptYXkgySmTE0nGgJ1zE0mSJOmxZnsOyzrgU0luAwp4MvBrc5ZKkiRpitkWlpOB5wInAq8CTmVQXCRJkubcbA8J/UFV3QscDfwSsAn4yzlLJUmSNMVsC8uu7vEM4INVdTlw2IHsOMmiJN9I8nfd9PIkVya5sXs85kC2L0mSFo7ZFpZtST4E/Crw+SSH78O6u7MO2Dpl+lxgc1WtZvA16nMPcPuSJGmBmO05LL8KvBR4X1XdnWQl8Nb93WmSpzAYrbkA+N1u9pnAad3zi4EvAW/f331I0r665f5FvPsab6zZgh0PDj4TH7/0Jz0nEQz+Nlb3nGFWhaWqHgQ+M2V6O7D9APb7AeBtwBOmzDu+2y5VtT3JcTOtmOQc4ByAE0888QAiSNJPeRPHtvx4fByAw0/yv0sLVtP/38hsR1gOmiQvB26vqquTnLav61fVJgYn/TI2NuY3lSQdFN7stC3e6FTTDb2wAC8EfiXJy4AjgKOSfBzYkWRlN7qyEri9h2ySJKlBB3ri7D6rqt+vqqdU1QhwFvDFqnodcAWwpltsDXD5sLNJkqQ2Db2w7MF7gV9KciODa728t+c8kiSpEX0cEnpUVX2JwbeBqKo7gdP7zCNJktrU0giLJEnSjCwskiSpeRYWSZLUPAuLJElqnoVFkiQ1z8IiSZKaZ2GRJEnNs7BIkqTm9XrhOA3Pxo0bGe/ufjqfTb6HyRujzWejo6PecE+SZsnConllyZIlfUeQJPXAwnKI8JO8JGk+8xwWSZLUPAuLJElqnoVFkiQ1z8IiSZKaZ2GRJEnNs7BIkqTmWVgkSVLzLCySJKl5FhZJktS8oReWJCck+ackW5Ncn2RdN395kiuT3Ng9HjPsbJIkqU19jLA8AvxeVT0DOBV4U5JnAucCm6tqNbC5m5YkSRp+Yamq7VV1Tff8PmArsAo4E7i4W+xi4JXDziZJktrU6zksSUaA5wJfA46vqu0wKDXAcf0lkyRJLemtsCRZBvwN8N+r6t59WO+cJFuSbJmYmJi7gJIkqRm9FJYkj2dQVi6pqs90s3ckWdm9vhK4faZ1q2pTVY1V1diKFSuGE1iSJPWqj28JBbgQ2FpV75/y0hXAmu75GuDyYWeTJEltWtzDPl8IvB74VpJru3nvAN4LXJbkbOAW4NU9ZJMkSQ0aemGpqi8D2c3Lpw8ziyRJmh+80q0kSWqehUWSJDXPwiJJkppnYZEkSc2zsEiSpOZZWCRJUvMsLJIkqXkWFkmS1DwLiyRJap6FRZIkNc/CIkmSmmdhkSRJzbOwSJKk5llYJElS8ywskiSpeRYWSZLUPAuLJElqnoVFkiQ1z8IiSZKaZ2GRJEnNs7BoXhkfH+eMM85gfHy87yiSpCFqrrAkeWmS7yQZT3Ju33nUlvXr1/PAAw+wfv36vqNIkoaoqcKSZBHw58B/Bp4JvCbJM/tNpVaMj49z0003AXDTTTc5yiJJh5DFfQeY5vnAeFV9DyDJpcCZwLd7TaUmTB9VWb9+PRdddFE/YaRGbdy4cUGU+cn3sG7dup6THLjR0VHWrl3bd4x5r6kRFmAV8IMp07d28x6V5JwkW5JsmZiYGGo49WtydGV305IWjiVLlrBkyZK+Y6ghrY2wZIZ59ZiJqk3AJoCxsbGaYXktUCMjI48pKSMjI71lkVrlJ3ktVK2NsNwKnDBl+inAbT1lUWPOO++8PU5Lkhau1grL14HVSU5OchhwFnBFz5nUiNHR0UdHVUZGRhgdHe03kCRpaJoqLFX1CPA7wN8DW4HLqur6flOpJeeddx5HHnmkoyuSdIhJ1fw9DWRsbKy2bNnSdwxJknSQJLm6qsamz29qhEWSJGkmFhZJktS8eX1IKMkEcHPfOTR0xwJ39B1C0pzzb/3QdFJVrZg+c14XFh2akmyZ6fimpIXFv3VN5SEhSZLUPAuLJElqnoVF89GmvgNIGgr/1vUoz2GRJEnNc4RFkiQ1z8KieSXJq5JUkqf3nUXSwZfkSUmu7X5+mGTblOnD+s6n/nhISPNKksuAlcDmqjq/5ziS5lCS84H7q+p9fWdR/xxh0byRZBnwQuBsBnfyliQdIiwsmk9eCXyhqr4L3JXklL4DSZKGw8Ki+eQ1wKXd80u7aUnSIWBx3wGk2UjyJOAXgWclKWARUEneVp6IJUkLniMsmi/+C/DRqjqpqkaq6gTg+8CLes4lSRoCC4vmi9cA/3vavL8Bfr2HLJKkIfNrzZIkqXmOsEiSpOZZWCRJUvMsLJIkqXkWFkmS1DwLiyRJap6FRdKcSrKru9PudUk+lWTpHpZ9xyy3OavlJC0cfq1Z0pxKcn9VLeueXwJcXVXv39uys92mpEODIyyShulfgNEkK5NcNWXk5T8meS+wpJt3CUCSzya5Osn1Sc7p5j1muSQjSa6b3EGStyQ5v3v+5iTfTvLNJJf+bBxJ84UjLJLm1ORoSJLFDK5O/AVgKXBEVV2QZBGwtKrumz5ykmR5Vd2VZAnwdeAXqurOaaM2I8DfVdWzuum3AMuq6vwktwEnV9VDSY6uqruH+d4lHTze/FDSXFuS5Nru+b8AFwKnAh9O8njgs1V17W7WfXOSV3XPTwBWA3fuw76/CVyS5LPAZ/c9uqRWeEhI0lzbWVXP6X7WVtWPq+oq4MXANuBjSd4wfaUkpwEvAV5QVc8GvgEcMcP2H+Gx/y+buswZwJ8DzwOu7kZ5JM1DFhZJQ5fkJOD2qvorBiMup3QvPdyNugA8EfjXqnowydMZjMoww3I7gOOSPCnJ4cDLu308Djihqv4JeBtwNOCJutI85acNSX04DXhrkoeB+4HJEZZNwDeTXAO8EfitJN8EvgN8dcr6jy5XVa9N8kfA14DvAzd0yywCPp7kiUCAP/McFmn+8qRbSZLUPA8JSZKk5llYJElS8ywskiSpeRYWSZLUPAuLJElqnoVFkiQ1z8IiSZKaZ2GRJEnN+/+pl/MgxJmKWwAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiwAAADgCAYAAAAgwj0PAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAaxUlEQVR4nO3de5hddX3v8feHBEgwyqUEjIwY20Rbauttjket5kTBttpalCrQWo2t53B6sdG2tqLFIypa2moPTT1e0mqJrXKKSAWx5ygEkIpWHS4VSEozlYsDEYIKcgloyLd/7BXcmczABGbPWjN5v55nP3uvtX5rre8eFjOf/H7rkqpCkiSpy/ZquwBJkqSHYmCRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRNGVJKsmyadrWoUkuSXJnkvdNxzbblOT0JKc0n5+f5Nq2a5LmEgOLNAsluT7J1iR3Jfluks8meXzbde2Q5LVJvvgQzU4AbgMeU1V/MANlzZiq+ueqenLbdUhziYFFmr1eWlWLgCXALcBftVzP7noCsKEext0rk8wfQD27s/95be5f2hMZWKRZrqruBc4CjtgxL8n+ST6WZEuSG5KclGSvJAclGUvy0qbdoiSjSV7TTJ+e5ENJzm+Gar6Q5AkT7fdB9vETwIeA5zQ9QLdPsO7pwCrgj5o2RyXZN8lpSW5uXqcl2bdpv7Kp+81JvgX87QTbnJfkfUluS3Jdktc3Q1jzm+XXJzmqr/3JSf6+b/qTSb6V5I5mqOon++tN8sEk/5TkbuAFSZ6e5PLm5/QPwIK+9iuTjPVNn5jkP5q2G5K8vG/Za5N8Mcl7m96y65K8eLL/3tKeysAizXJJ9gOOA/6lb/ZfAfsDPwr8N+A1wK9X1XeA3wD+OskhwP8Grqyqj/Wt+yrgXcDBwJXAxyfZ9WT72Aj8JvDlqlpUVQeMX7GqXtts98+aNhcAfww8G3ga8FTgWcBJfas9FjiIXs/MCRPU8z+AFzfrPwN42SR1T+b/AcuBQ4DL2fV7/yrwbuDRwFeBTwN/19T0SeCXH2Tb/wE8n97P6x3A3ydZ0rf8vwLX0vuZ/xnwkSTZzfqlOc3AIs1en256L74HvAj4c3hguOI44C1VdWdVXQ+8D3g1QFV9nt4f2PXALwD/c9x2P1tVl1TVffRCxHPGnx/zUPt4mF4FvLOqbq2qLfT+sPdvbzvw9qq6r6q2TrD+scBfVtVYVX0XOHV3dl5VH22+y33AycBTk+zf1+Scqrq0qrbTC0V7A6dV1Q+q6izgaw+y7U9W1c1Vtb2q/gHYRC+Q7XBDVf11Vd0PrKM3zHfo7tQvzXUGFmn2elnTe7Ev8HrgC0keS+9f6fsAN/S1vQE4rG96LfAU4G+r6tvjtvvNHR+q6i7gO8DjxrWZyj521+Mm2F7/frc0w18Ptv43+6a/OVnD8ZrhpFObYZvvAdc3iw6eZHuPA24ad/5Nf+3jt/+aJFcmub0JmU8Zt+1v7fhQVfc0HxdNtX5pT2BgkWa5qrq/qs4G7geeR+/Kmx/QGzrZ4XDgJnigd+TDwMeA35rgMuUHelOSLKI35HHzuDYPug/g4TwG/uYJtte/34fa5mZgqG96/FVTdwP79U0/tu/zrwJHA0fRG7ZZ2szvH5bp3/9m4LBxwzaHT1RUcw7QX9MLlT/ShMyrx21b0kMwsEizXHqOBg4ENjbDCmcC707y6OYP5u8DO04wfWvz/hvAe4GPjbvq5SVJnpdkH3rnsnylqnbqrZjCPm4BhpptTNUZwElJFic5GPhffdubijOBNyQ5LMkBwJvHLb8SOD7J3kmGgVf0LXs0cB/wbXqh5j0Psa8vA9uA1UnmJzmGnYd4+j2KXtjZApDk1+n1sEjaDQYWafb6TJK76J3D8m5gVVVd0yz7XXo9Ct8Avgh8AvhokmfSCxavaULHn9L7Y3pi33Y/Abyd3lDQM+mdWzKRCffRLLsQuAb4VpLbpvh9TgFGgK8DV9E78fWUKa4LvV6MzzfrXwH8E71QcX+z/G3AjwHfpXd+zCf61v0YvSGdm4AN7HwC8y6q6vvAMcBrm+0dB5w9SdsN9M7v+TK9IPdTwKW78b0kAXkYt0CQNEc1lxuPVdVJD9W265pLgz9UVRNeli1pdrGHRdKckGRhkpc0QzSH0esl+se265I0PQwskuaK0Bvq+S69IaGN9M6DkTQHOCQkSZI6zx4WSZLUeQYWSZLUea0+8fSROvjgg2vp0qVtlyFJkqbJZZdddltVLR4/f1YHlqVLlzIyMtJ2GZIkaZokmfAxFw4JSZKkzjOwSJKkzhtYYEny0SS3Jrm6b95BSc5Psql5P7Bv2VuSjCa5NsnPDaouSZI0+wyyh+V04OfHzTsRWF9Vy4H1zTRJjgCOB36yWecD4x7GJkmS9mADO+m2qi5JsnTc7KOBlc3ndcDF9J6oejTwf6vqPuC6JKP0nnz65UHV1yVr1qxhdHS01RrGxsYAGBoaarUOgGXLlrF69eq2y5AkdchMn8NyaFVtBmjeD2nmHwb0P75+rJm3iyQnJBlJMrJly5aBFrsn2bp1K1u3bm27DEmSJtSVy5ozwbwJnxlQVWuBtQDDw8Nz4rkCXehN2FHDmjVrWq5EkqRdzXQPyy1JlgA077c288eAx/e1GwJunuHaJElSR810YDkXWNV8XgWc0zf/+CT7JnkisBz46gzXJkmSOmpgQ0JJzqB3gu3BScaAtwOnAmcmeR1wI/BKgKq6JsmZwAZgG/A7VXX/oGqTJEmzyyCvEvqVSRYdOUn7dwPvHlQ9kiRp9vJOt5IkqfMMLJIkqfMMLJIkqfMMLJIkqfMMLJIkqfMMLJIkqfMMLJIkqfMMLJIkqfO68vBDSR20Zs0aRkdHW61hbGwMgKGhoVbrAFi2bFknHlaqbhyb0J3jc084Ng0skjpt69atbZcgTcrjc+YYWCRNqgv/YttRw5o1a1quRF3ShWMTPD5nkuewSJKkzjOwSJKkzjOwSJKkzjOwSJKkzjOwSJKkzjOwSJKkzjOwSJKkzjOwSJKkzjOwSJKkzmslsCT5vSTXJLk6yRlJFiQ5KMn5STY17we2UZskSeqeGQ8sSQ4DVgPDVfUUYB5wPHAisL6qlgPrm2lJkqTWhoTmAwuTzAf2A24GjgbWNcvXAS9rqTZJktQxMx5Yquom4L3AjcBm4I6q+jxwaFVtbtpsBg6Z6dokSVI3tTEkdCC93pQnAo8DHpXk13Zj/ROSjCQZ2bJly6DKlCRJHdLGkNBRwHVVtaWqfgCcDTwXuCXJEoDm/daJVq6qtVU1XFXDixcvnrGiJUlSe9oILDcCz06yX5IARwIbgXOBVU2bVcA5LdQmSZI6aP5M77CqvpLkLOByYBtwBbAWWAScmeR19ELNK2e6NkmS1E0zHlgAqurtwNvHzb6PXm+LJEnSTrzTrSRJ6jwDiyRJ6jwDiyRJ6jwDiyRJ6jwDiyRJ6jwDiyRJ6jwDiyRJ6jwDiyRJ6jwDiyRJ6rxW7nTbFWvWrGF0dLTtMjph06ZNAKxevbrlSrph2bJl/iwkqUP26MAyOjrKFVdtYPt+B7VdSuvy/QLgsv/4VsuVtG+ve77TdgmSpHH26MACsH2/g7j3iF9suwx1yIIN57VdgiRpnD0+sEhd5HDlDzlcuTOHK7WnMrBIHTQ6Osq/X305hy+6v+1SWrfPD3rXBtx7/ddarqR9N941r+0SpNYYWKSOOnzR/Zw0fFfbZahDThlZ1HYJUmu8rFmSJHWePSySpN3iOVY/5DlWOxvkOVYGFknSbhkdHeWKa66AA9qupAO2996uuOmKduvogtsHu3kDiyRp9x0A21dub7sKdcheFw/2LBPPYZEkSZ1nYJEkSZ3XSmBJckCSs5L8W5KNSZ6T5KAk5yfZ1Lwf2EZtkiSpe9rqYflL4P9X1Y8DTwU2AicC66tqObC+mZYkSZr5wJLkMcAK4CMAVfX9qrodOBpY1zRbB7xspmuTJEnd1EYPy48CW4C/TXJFkr9J8ijg0KraDNC8HzLRyklOSDKSZGTLli0zV7UkSWpNG4FlPvAM4INV9XTgbnZj+Keq1lbVcFUNL168eFA1SpKkDmkjsIwBY1X1lWb6LHoB5pYkSwCa91tbqE2SJHXQjAeWqvoW8M0kT25mHQlsAM4FVjXzVgHnzHRtkiSpm6Z8p9skC4HDq+raadjv7wIfT7IP8A3g1+mFpzOTvA64EXjlNOxHkiTNAVMKLEleCrwX2Ad4YpKnAe+sql96ODutqiuB4QkWHflwtidJkua2qQ4JnQw8i+bRRk3gWDqYkiRJknY21SGhbVV1R5KBFjPTxsbG2OueO1iw4by2S1GH7HXPtxkb29ZqDWNjY9x95zxOGVnUah3qlhvunMejxsbaLkNqxVQDy9VJfhWYl2Q5sBr40uDKkiRJ+qGpBpbfBf4YuA/4BPA54JRBFTVThoaGuOW++dx7xC+2XYo6ZMGG8xgaemyrNQwNDXHvts2cNHxXq3WoW04ZWcSCoaG2y5Ba8ZCBJck84NyqOopeaJEkSZpRD3nSbVXdD9yTZP8ZqEeSJGkXUx0Suhe4Ksn59G6lD0BVrR5IVZIkSX2mGlg+27wkSZJm3JQCS1Wta+5K+6Rm1rVV9YPBlSVJ6qqxsTG4A/a6uI3H0amzboexGtxl91O90+1KYB1wPRDg8UlWVdUlA6tMkiSpMdUhofcBP7vjOUJJngScATxzUIVJkrppaGiILdnC9pXb2y5FHbLXxXsxdNjgLrufan/e3v0PPayqfwf2HkxJkiRJO5tqD8tIko8Af9dMvwq4bDAlSZIk7WyqgeW3gN+hd0v+AJcAHxhUUZIkSf2mGljmA39ZVX8BD9z9dt+BVSVJktRnquewrAcW9k0vBC6Y/nIkSZJ2NdUelgVV9cBT2KrqriT7DagmScCNd83jlJFFbZfRulvu6f276tD9vCLlxrvmPXAzLGlPM9XAcneSZ1TV5QBJhoGtgytL2rMtW7as7RI64/ubNgGwYOnylitp35Pw2NCea6qB5Q3AJ5PcDBTwOOC4gVUl7eFWr/YxXTvs+FmsWbOm5UoktWmqgeWJwNOBw4GXA8+mF1wkSZIGbqon3b6tqr4HHAC8CFgLfHBgVUmSJPWZamC5v3n/BeBDVXUOsM8j2XGSeUmuSHJeM31QkvOTbGreD3wk25ckSXPHVAPLTUk+DBwL/FOSfXdj3cm8AdjYN30isL6qltO7jPrER7h9SZI0R0z1HJZjgZ8H3ltVtydZAvzhw91pkiF6vTXvBn6/mX00sLL5vA64GHjzw93HVO11z3dYsOG8Qe+m83Lv9wCoBY9puZL27XXPd4DHtl2G1G239x5215q7gG3t7b5z5gNt3wXhduCwwW1+SoGlqu4Bzu6b3gxsfgT7PQ34I+DRffMObbZLVW1OcshEKyY5ATgB4PDDD38EJXh5YL9Nm+4EYPmP+YcaHuuxIT2ILvz/MTY2xtat3l1jh4ULFw70SclTcthgj42p9rBMmyS/CNxaVZclWbm761fVWnon/TI8PPyIrlTy0tEf8tJRSVPl7061YcYDC/AzwC8leQmwAHhMkr8HbkmypOldWQLc2kJtkiSpg2Z8ALKq3lJVQ1W1FDgeuLCqfg04F1jVNFsFnDPTtUmSpG5q8YypXZwKvCjJJnr3ejm15XokSVJHtDEk9ICqupje1UBU1beBI9usR5IkdVOXelgkSZImZGCRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdN7/tAiR115o1axgdHW21hk2bNgGwevXqVusAWLZsWSfqkPZEBhZJnbZw4cK2S5DUAQYWSZOyN0FSV3gOiyRJ6jwDiyRJ6rwZDyxJHp/koiQbk1yT5A3N/IOSnJ9kU/N+4EzXJkmSuqmNHpZtwB9U1U8AzwZ+J8kRwInA+qpaDqxvpiVJkmY+sFTV5qq6vPl8J7AROAw4GljXNFsHvGyma5MkSd3U6jksSZYCTwe+AhxaVZuhF2qAQ9qrTJIkdUlrgSXJIuBTwBur6nu7sd4JSUaSjGzZsmVwBUqSpM5oJbAk2ZteWPl4VZ3dzL4lyZJm+RLg1onWraq1VTVcVcOLFy+emYIlSVKr2rhKKMBHgI1V9Rd9i84FVjWfVwHnzHRtkiSpm9q40+3PAK8GrkpyZTPvrcCpwJlJXgfcCLyyhdokSVIHzXhgqaovAplk8ZEzWYskSZodvNOtJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLJEnqPAOLpE477bTTWLFiBe9///vbLkXaxQUXXMCKFSu46KKL2i5lzutcYEny80muTTKa5MS265HUrrPPPhuAM888s+VKpF295z3vAeBd73pXy5XMfZ0KLEnmAf8HeDFwBPArSY5otypJbTnttNN2mraXRV1ywQUXsG3bNgC2bdtmL8uApararuEBSZ4DnFxVP9dMvwWgqv5kovbDw8M1MjIygxUOxpo1axgdHW21hk2bNgGwfPnyVusAWLZsGatXr267DHXAihUrdpl3ySWXtFCJtKsXvvCFDwQWgPnz53PhhRe2WNHckOSyqhoeP79TPSzAYcA3+6bHmnkPSHJCkpEkI1u2bJnR4uayhQsXsnDhwrbLkKRZoz+sTDSt6TW/7QLGyQTzduoCqqq1wFro9bDMRFGDZm+CJM0+8+fP36WHRYPTtR6WMeDxfdNDwM0t1SKpZcccc8xO08cee2xLlUi7eutb37rT9Nve9raWKtkzdC2wfA1YnuSJSfYBjgfObbkmSS154xvfuNP061//+pYqkXZ11FFHPdCrMn/+fF7wghe0XNHc1qnAUlXbgNcDnwM2AmdW1TXtViWpTTt6WexdURft6GWxd2XwOnWV0O6aK1cJSZKkntlylZAkSdIuDCySJKnzZvWQUJItwA1t1zGHHAzc1nYR0gQ8NtVlHp/T6wlVtXj8zFkdWDS9koxMNG4otc1jU13m8TkzHBKSJEmdZ2CRJEmdZ2BRv7VtFyBNwmNTXebxOQM8h0WSJHWePSySJKnzDCwiycokz+2bPj3JK9qsSXNXktVJNib5+CTLn5bkJX3TJyd508xVKO0syQFJfrtvemWS89qsaU9kYBHASuC5D9VoKtLjcaUH89vAS6rqVZMsfxrwkkmW7bYk86ZrW9pjHUDvuJ0WSeZP17b2JP5hmSOSLE3yb0n+JsnVST6e5KgklybZlORZSQ5K8ukkX0/yL0l+OslS4DeB30tyZZLnN5tckeRLSb7R39uS5A+TfK3Zxjv69r0xyQeAy4HHz/DX1yyR5EPAjwLnJnlzc4xd0bw/uXlK+zuB45rj8bhm1SOSXNwcj6v7tvdrSb7atP3wjnCS5K4k70zyFeA5M/09Nbsl+f3m9+jVSd4InAr8WHOc/XnTbFGSs5rfux9PkmbdZyb5QpLLknwuyZJm/sVJ3pPkC8Ab2vlms1xV+ZoDL2ApsA34KXpB9DLgo0CAo4FPA38FvL1p/0LgyubzycCb+rZ1OvDJZjtHAKPN/J+ldzZ8mmXnASuafW8Hnt32z8FX91/A9fTuDPoYYH4z7yjgU83n1wLv72t/MvAlYN9mvW8DewM/AXwG2Ltp9wHgNc3nAo5t+7v6mn0v4JnAVcCjgEXANcDTgav72qwE7gCGmt+FXwae1xyXXwIWN+2OAz7afL4Y+EDb3282v+yWmluuq6qrAJJcA6yvqkpyFb1Q8QTglwGq6sIkP5Jk/0m29emq2g5sSHJoM+9nm9cVzfQiYDlwI3BDVf3LIL6U5qz9gXVJltMLGHs/SNvPVtV9wH1JbgUOBY6k98fla80/bhcCtzbt7wc+NajCNac9D/jHqrobIMnZwPMnaPfVqhpr2lxJ73fs7cBTgPObY3IesLlvnX8YXNlzn4Flbrmv7/P2vunt9P5bb5tgncmua+/fVvre/6SqPtzfsBlWuns3a5XeBVxUVS9vjqGLH6Rt//F4P73jOcC6qnrLBO3vrar7p6lO7Vny0E2AyY/Ja6pqsmFIf08+Ap7Dsme5BHgV9M5yB26rqu8BdwKPnsL6nwN+I8miZhuHJTlkQLVq7tsfuKn5/Nq++VM9HtcDr9hxDDbnaD1hWivUnugS4GVJ9kvyKODlwKVM7Zi8Flic5DkASfZO8pODK3XPYmDZs5wMDCf5Or2TyFY18z8DvHzcSbe7qKrPA58AvtwMM53F1P4nlibyZ8CfJLmUXtf5DhfRO8m2/6TbXVTVBuAk4PPNMX0+sGSQBWvuq6rL6Z3H91XgK8DfVNVlwKXNSbh//iDrfh94BfCnSf4VuJJpugJT3ulWkiTNAvawSJKkzjOwSJKkzjOwSJKkzjOwSJKkzjOwSJKkzjOwSJqV+p8q3jxD64i2a5I0ON7pVlLnJZn3YHeurar/PpP1SJp59rBImnZJ3tY8xfb8JGckeVPztNrhZvnBSa5vPi9N8s9JLm9ez23mr0xyUZJPAFel5/1JNiT5LHBI3/76t/3BJCNJrtnxRPFm/vVJ3tHs46okPz6DPxJJj5A9LJKmVRMcfpneE27nA5fTe3r4ZG4FXlRV9zYPQjwDGG6WPQt4SlVdl+QY4Mn0nkh+KLCB3hPJx/vjqvpOknnA+iQ/XVVfb5bdVlXPSPLbwJsAe2akWcLAImm6PQ84p6q2AiT5zEO03xt4f5Kn0XuI3JP6ln21qq5rPq8AzmiGhm5OcuEk2zs2yQn0fr8tAY4AdgSWs5v3y4BjduM7SWqZgUXSdJvsabfb+OEw9IK++b8H3AI8tVl+b9+y8U+3fdBniSR5Ir2ek/9SVd9Ncvq4fe14wu6Op+tKmiU8h0XSdPsi8NIkC5one/9CM/964JnN51f0td8f2FxV24FXs/ODEPtdAhyfZF6SJcALJmjzGHoh544khwIvfkTfRFJn+C8MSdOqqr6W5FzgX4EbgBHgDuC9wJlJXg30D+d8APhUklfSe1Lz+F6VHf4ReCFwFfDvwBcm2Pe/JrkCuAb4BnDptHwpSa3zac2Spl2SRVV1V5L96PWMnFBVl7ddl6TZyx4WSYOwtrmR2wJgnWFF0iNlD4skSeo8T7qVJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmdZ2CRJEmd95+BP62apdeI8QAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x216 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "for col in ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu',\n",
    "            'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime',\n",
    "            'failures', 'famsup', 'schoolsup', 'paid', 'activities', 'nursery',\n",
    "            'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'health']:\n",
    "    get_boxplot(col)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It seems that many attributes can have an influence on the score, so we can select just significant ones with Student's t-test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Student's t-test for nominal attributes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_stat_dif(column):\n",
    "    cols = data_math[column].dropna().unique()\n",
    "    combinations_all = list(combinations(cols, 2))\n",
    "    for comb in combinations_all:\n",
    "        if ttest_ind(data_math.loc[data_math.loc[:, column] == comb[0], 'score'].dropna(),\n",
    "                     data_math.loc[data_math.loc[:, column] == comb[1], 'score'].dropna()).pvalue \\\n",
    "                <= 0.05/len(combinations_all):\n",
    "            print('Statistically significant differences found for column', column)\n",
    "            break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Statistically significant differences found for column sex\n",
      "Statistically significant differences found for column address\n",
      "Statistically significant differences found for column Medu\n",
      "Statistically significant differences found for column Mjob\n",
      "Statistically significant differences found for column failures\n",
      "Statistically significant differences found for column paid\n",
      "Statistically significant differences found for column higher\n",
      "Statistically significant differences found for column romantic\n"
     ]
    }
   ],
   "source": [
    "for col in ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu',\n",
    "            'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime',\n",
    "            'failures', 'famsup', 'schoolsup', 'paid', 'activities', 'nursery',\n",
    "            'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'health']:\n",
    "    get_stat_dif(col)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### According to correlation analysis and Student's t-test, we should leave just the following columns as it's considered significant:\n",
    "\n",
    "- sex\n",
    "- address\n",
    "- Medu\n",
    "- Mjob\n",
    "- failures\n",
    "- paid\n",
    "- higher\n",
    "- romantic\n",
    "- age\n",
    "- absences"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And now i'm going to drop the rest:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_math.drop(columns=['school', 'famsize', 'Pstatus', 'Fedu',\n",
    "                        'Fjob', 'reason', 'traveltime', 'studytime', 'guardian',\n",
    "                        'famsup', 'schoolsup', 'activities', 'nursery',\n",
    "                        'internet', 'famrel', 'freetime', 'goout', 'health'], axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>address</th>\n",
       "      <th>Medu</th>\n",
       "      <th>Mjob</th>\n",
       "      <th>failures</th>\n",
       "      <th>paid</th>\n",
       "      <th>higher</th>\n",
       "      <th>romantic</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>F</td>\n",
       "      <td>18</td>\n",
       "      <td>U</td>\n",
       "      <td>4.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>6.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>F</td>\n",
       "      <td>17</td>\n",
       "      <td>U</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>3.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>4.0</td>\n",
       "      <td>health</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>2.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>F</td>\n",
       "      <td>16</td>\n",
       "      <td>U</td>\n",
       "      <td>3.0</td>\n",
       "      <td>other</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  sex  age address  Medu     Mjob  failures paid higher romantic  absences  \\\n",
       "0   F   18       U   4.0  at_home       0.0   no    yes       no       6.0   \n",
       "1   F   17       U   1.0  at_home       0.0   no    yes       no       4.0   \n",
       "2   F   15       U   1.0  at_home       3.0  NaN    yes      NaN      10.0   \n",
       "3   F   15       U   4.0   health       0.0  yes    yes      yes       2.0   \n",
       "4   F   16       U   3.0    other       0.0  yes    yes       no       4.0   \n",
       "\n",
       "   score  \n",
       "0   30.0  \n",
       "1   30.0  \n",
       "2   50.0  \n",
       "3   75.0  \n",
       "4   50.0  "
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_math.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Preparation for modelling\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we see, some columns contain non-numeric values, so we need to convert it to numeric ones"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_math['sex'] = data_math['sex'].map({'F': 1, 'M': 0})\n",
    "data_math['address'] = data_math['address'].map({'U': 1, 'R': 0})\n",
    "data_math['paid'] = data_math['paid'].map({'yes': 1, 'no': 0})\n",
    "data_math['higher'] = data_math['higher'].map({'yes': 1, 'no': 0})\n",
    "data_math['romantic'] = data_math['romantic'].map({'yes': 1, 'no': 0})\n",
    "data_math['Mjob'] = data_math['Mjob'].map(\n",
    "    {'at_home': 0, 'health': 1, 'teacher': 2, 'services': 3, 'other': 4})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>address</th>\n",
       "      <th>Medu</th>\n",
       "      <th>Mjob</th>\n",
       "      <th>failures</th>\n",
       "      <th>paid</th>\n",
       "      <th>higher</th>\n",
       "      <th>romantic</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>18</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>17</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>15</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>15</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   sex  age  address  Medu  Mjob  failures  paid  higher  romantic  absences  \\\n",
       "0    1   18      1.0   4.0   0.0       0.0   0.0     1.0       0.0       6.0   \n",
       "1    1   17      1.0   1.0   0.0       0.0   0.0     1.0       0.0       4.0   \n",
       "2    1   15      1.0   1.0   0.0       3.0   NaN     1.0       NaN      10.0   \n",
       "3    1   15      1.0   4.0   1.0       0.0   1.0     1.0       1.0       2.0   \n",
       "4    1   16      1.0   3.0   4.0       0.0   1.0     1.0       0.0       4.0   \n",
       "\n",
       "   score  \n",
       "0   30.0  \n",
       "1   30.0  \n",
       "2   50.0  \n",
       "3   75.0  \n",
       "4   50.0  "
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_math.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Conclusions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- There is not much missed values, data is pretty clean and do not require much processing, as outliers were found just in 2 columns\n",
    "- Negative correlation between age and score shows that elder students have lower score\n",
    "- Positive correlation between age and absences shows that younger students tend to skip classes more often\n",
    "- Mother's education and job has an impact on the score, which is reasonable, considering the fact that the most of the guardians are mothers\n",
    "- Students who wants to get higher education show better results at the exam\n",
    "- Boys get better score for math, and romantic realtionships have some impact on the score\n",
    "- Kids living out of the city seem to be more distracted from the study. May be because of long way to school or due to extra daily responsibilities related to rural life\n",
    "- Kids whose parents pay for extra education use to have better scores\n",
    "- And of course some failures can disappoint and it's harder to move on, so its reflected on the score as well  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
