{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Fish_market.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "8ne-Eb0_Awbe"
      },
      "source": [
        "# Supress Warnings\n",
        "\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "k-YPRGUMBcXQ"
      },
      "source": [
        "# Import required libraries\n",
        "\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uJugtx5dBcbk"
      },
      "source": [
        "# Import data from github\n",
        "\n",
        "url = 'https://raw.githubusercontent.com/bhavna9719/fish_market/master/Fish.csv'\n",
        "fish = pd.read_csv(url)"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MhPMI1_rBcgc",
        "outputId": "778b2be0-143b-4822-d3e8-7ae77b3d9ed3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 197
        }
      },
      "source": [
        "# First 5 rows of df\n",
        "\n",
        "fish.head()"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Species</th>\n",
              "      <th>Weight</th>\n",
              "      <th>Length1</th>\n",
              "      <th>Length2</th>\n",
              "      <th>Length3</th>\n",
              "      <th>Height</th>\n",
              "      <th>Width</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Bream</td>\n",
              "      <td>242.0</td>\n",
              "      <td>23.2</td>\n",
              "      <td>25.4</td>\n",
              "      <td>30.0</td>\n",
              "      <td>11.5200</td>\n",
              "      <td>4.0200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Bream</td>\n",
              "      <td>290.0</td>\n",
              "      <td>24.0</td>\n",
              "      <td>26.3</td>\n",
              "      <td>31.2</td>\n",
              "      <td>12.4800</td>\n",
              "      <td>4.3056</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Bream</td>\n",
              "      <td>340.0</td>\n",
              "      <td>23.9</td>\n",
              "      <td>26.5</td>\n",
              "      <td>31.1</td>\n",
              "      <td>12.3778</td>\n",
              "      <td>4.6961</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Bream</td>\n",
              "      <td>363.0</td>\n",
              "      <td>26.3</td>\n",
              "      <td>29.0</td>\n",
              "      <td>33.5</td>\n",
              "      <td>12.7300</td>\n",
              "      <td>4.4555</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Bream</td>\n",
              "      <td>430.0</td>\n",
              "      <td>26.5</td>\n",
              "      <td>29.0</td>\n",
              "      <td>34.0</td>\n",
              "      <td>12.4440</td>\n",
              "      <td>5.1340</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  Species  Weight  Length1  Length2  Length3   Height   Width\n",
              "0   Bream   242.0     23.2     25.4     30.0  11.5200  4.0200\n",
              "1   Bream   290.0     24.0     26.3     31.2  12.4800  4.3056\n",
              "2   Bream   340.0     23.9     26.5     31.1  12.3778  4.6961\n",
              "3   Bream   363.0     26.3     29.0     33.5  12.7300  4.4555\n",
              "4   Bream   430.0     26.5     29.0     34.0  12.4440  5.1340"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zTF0-YmSBcjJ",
        "outputId": "b4d7db29-29e5-45c7-f16c-787d4d4357be",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# Rows and columns count\n",
        "\n",
        "fish.shape"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(159, 7)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W134ePp3BcrC",
        "outputId": "0608424f-02b0-4825-89db-9bec1ee76f28",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        }
      },
      "source": [
        "# Datatypes, null value check\n",
        "\n",
        "fish.info()"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 159 entries, 0 to 158\n",
            "Data columns (total 7 columns):\n",
            " #   Column   Non-Null Count  Dtype  \n",
            "---  ------   --------------  -----  \n",
            " 0   Species  159 non-null    object \n",
            " 1   Weight   159 non-null    float64\n",
            " 2   Length1  159 non-null    float64\n",
            " 3   Length2  159 non-null    float64\n",
            " 4   Length3  159 non-null    float64\n",
            " 5   Height   159 non-null    float64\n",
            " 6   Width    159 non-null    float64\n",
            "dtypes: float64(6), object(1)\n",
            "memory usage: 8.8+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ey7hh6ZwDPNW",
        "outputId": "670e1818-b88a-4618-8806-14444d47561d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 287
        }
      },
      "source": [
        "# Statistical data of df\n",
        "\n",
        "fish.describe()"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Weight</th>\n",
              "      <th>Length1</th>\n",
              "      <th>Length2</th>\n",
              "      <th>Length3</th>\n",
              "      <th>Height</th>\n",
              "      <th>Width</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>159.000000</td>\n",
              "      <td>159.000000</td>\n",
              "      <td>159.000000</td>\n",
              "      <td>159.000000</td>\n",
              "      <td>159.000000</td>\n",
              "      <td>159.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>398.326415</td>\n",
              "      <td>26.247170</td>\n",
              "      <td>28.415723</td>\n",
              "      <td>31.227044</td>\n",
              "      <td>8.970994</td>\n",
              "      <td>4.417486</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>357.978317</td>\n",
              "      <td>9.996441</td>\n",
              "      <td>10.716328</td>\n",
              "      <td>11.610246</td>\n",
              "      <td>4.286208</td>\n",
              "      <td>1.685804</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>7.500000</td>\n",
              "      <td>8.400000</td>\n",
              "      <td>8.800000</td>\n",
              "      <td>1.728400</td>\n",
              "      <td>1.047600</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>120.000000</td>\n",
              "      <td>19.050000</td>\n",
              "      <td>21.000000</td>\n",
              "      <td>23.150000</td>\n",
              "      <td>5.944800</td>\n",
              "      <td>3.385650</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>273.000000</td>\n",
              "      <td>25.200000</td>\n",
              "      <td>27.300000</td>\n",
              "      <td>29.400000</td>\n",
              "      <td>7.786000</td>\n",
              "      <td>4.248500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>650.000000</td>\n",
              "      <td>32.700000</td>\n",
              "      <td>35.500000</td>\n",
              "      <td>39.650000</td>\n",
              "      <td>12.365900</td>\n",
              "      <td>5.584500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>1650.000000</td>\n",
              "      <td>59.000000</td>\n",
              "      <td>63.400000</td>\n",
              "      <td>68.000000</td>\n",
              "      <td>18.957000</td>\n",
              "      <td>8.142000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            Weight     Length1     Length2     Length3      Height       Width\n",
              "count   159.000000  159.000000  159.000000  159.000000  159.000000  159.000000\n",
              "mean    398.326415   26.247170   28.415723   31.227044    8.970994    4.417486\n",
              "std     357.978317    9.996441   10.716328   11.610246    4.286208    1.685804\n",
              "min       0.000000    7.500000    8.400000    8.800000    1.728400    1.047600\n",
              "25%     120.000000   19.050000   21.000000   23.150000    5.944800    3.385650\n",
              "50%     273.000000   25.200000   27.300000   29.400000    7.786000    4.248500\n",
              "75%     650.000000   32.700000   35.500000   39.650000   12.365900    5.584500\n",
              "max    1650.000000   59.000000   63.400000   68.000000   18.957000    8.142000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6K9u4POlBcyA",
        "outputId": "9ca826d5-7821-46a3-c42c-9aaf4217bf06",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 278
        }
      },
      "source": [
        "# Species count graph\n",
        "\n",
        "sns.countplot(fish.Species)\n",
        "plt.show()"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JgUQrTtzBcvz",
        "outputId": "aa45e7cf-c627-40ac-8b66-ea03cf6ba3f0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 268
        }
      },
      "source": [
        "# Correlation check\n",
        "\n",
        "sns.heatmap(fish.corr(), annot = True, cmap = \"Greens\")\n",
        "plt.show()"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "T5Ss0kruBcuL"
      },
      "source": [
        "# Can conclude that every column has a good correlation with target variable"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1-Lb2-sIBcqC",
        "outputId": "fc73a96a-946b-401f-e16a-091da0f07865",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 197
        }
      },
      "source": [
        "# Create dummies and merge\n",
        "\n",
        "fish_dum = pd.get_dummies(fish['Species'], drop_first = True)\n",
        "fish = pd.concat([fish, fish_dum], axis = 1)\n",
        "fish.drop( \"Species\", axis = 1, inplace = True)\n",
        "fish.head()"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Weight</th>\n",
              "      <th>Length1</th>\n",
              "      <th>Length2</th>\n",
              "      <th>Length3</th>\n",
              "      <th>Height</th>\n",
              "      <th>Width</th>\n",
              "      <th>Parkki</th>\n",
              "      <th>Perch</th>\n",
              "      <th>Pike</th>\n",
              "      <th>Roach</th>\n",
              "      <th>Smelt</th>\n",
              "      <th>Whitefish</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>242.0</td>\n",
              "      <td>23.2</td>\n",
              "      <td>25.4</td>\n",
              "      <td>30.0</td>\n",
              "      <td>11.5200</td>\n",
              "      <td>4.0200</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>290.0</td>\n",
              "      <td>24.0</td>\n",
              "      <td>26.3</td>\n",
              "      <td>31.2</td>\n",
              "      <td>12.4800</td>\n",
              "      <td>4.3056</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>340.0</td>\n",
              "      <td>23.9</td>\n",
              "      <td>26.5</td>\n",
              "      <td>31.1</td>\n",
              "      <td>12.3778</td>\n",
              "      <td>4.6961</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>363.0</td>\n",
              "      <td>26.3</td>\n",
              "      <td>29.0</td>\n",
              "      <td>33.5</td>\n",
              "      <td>12.7300</td>\n",
              "      <td>4.4555</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>430.0</td>\n",
              "      <td>26.5</td>\n",
              "      <td>29.0</td>\n",
              "      <td>34.0</td>\n",
              "      <td>12.4440</td>\n",
              "      <td>5.1340</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Weight  Length1  Length2  Length3  ...  Pike  Roach  Smelt  Whitefish\n",
              "0   242.0     23.2     25.4     30.0  ...     0      0      0          0\n",
              "1   290.0     24.0     26.3     31.2  ...     0      0      0          0\n",
              "2   340.0     23.9     26.5     31.1  ...     0      0      0          0\n",
              "3   363.0     26.3     29.0     33.5  ...     0      0      0          0\n",
              "4   430.0     26.5     29.0     34.0  ...     0      0      0          0\n",
              "\n",
              "[5 rows x 12 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "02VSyRViBceL"
      },
      "source": [
        "# Import required library\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "# Train and test df split\n",
        "np.random.seed(0)\n",
        "fish_train, fish_test = train_test_split( fish, train_size = 0.7, test_size = 0.3, random_state = 100)"
      ],
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KjwxYYLXFpKG",
        "outputId": "8e205a4b-d495-4195-a49d-c85990346f8c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# Row and column count of train df\n",
        "\n",
        "fish_train.shape"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(111, 12)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KW7PSIGfFpHs",
        "outputId": "bc3aa999-a958-4435-8d85-aceb6eabd6ce",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# Row and column count of test df\n",
        "\n",
        "fish_test.shape"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(48, 12)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "u9BsBcWNFCGB"
      },
      "source": [
        "# Import required library\n",
        "\n",
        "from sklearn.preprocessing import StandardScaler"
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "50M_gDJwFCJT"
      },
      "source": [
        "# Standard scaler \n",
        "\n",
        "scaler = StandardScaler()"
      ],
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9Bl4cYIqFCPF"
      },
      "source": [
        "# scaler() to all the columns except the 'dummy' variables\n",
        "\n",
        "num_vars = ['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']\n",
        "\n",
        "fish_train[num_vars] = scaler.fit_transform(fish_train[num_vars])"
      ],
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yBQFSGgLFwUd",
        "outputId": "5ba25b60-1fd0-486e-8fac-5791f8f263ae",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 287
        }
      },
      "source": [
        "# Statistical data of train df\n",
        "\n",
        "fish_train.describe()"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Weight</th>\n",
              "      <th>Length1</th>\n",
              "      <th>Length2</th>\n",
              "      <th>Length3</th>\n",
              "      <th>Height</th>\n",
              "      <th>Width</th>\n",
              "      <th>Parkki</th>\n",
              "      <th>Perch</th>\n",
              "      <th>Pike</th>\n",
              "      <th>Roach</th>\n",
              "      <th>Smelt</th>\n",
              "      <th>Whitefish</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>1.110000e+02</td>\n",
              "      <td>1.110000e+02</td>\n",
              "      <td>1.110000e+02</td>\n",
              "      <td>1.110000e+02</td>\n",
              "      <td>1.110000e+02</td>\n",
              "      <td>1.110000e+02</td>\n",
              "      <td>111.000000</td>\n",
              "      <td>111.000000</td>\n",
              "      <td>111.000000</td>\n",
              "      <td>111.000000</td>\n",
              "      <td>111.000000</td>\n",
              "      <td>111.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>-2.675537e-17</td>\n",
              "      <td>5.243553e-16</td>\n",
              "      <td>3.035610e-16</td>\n",
              "      <td>4.905986e-16</td>\n",
              "      <td>-1.200241e-17</td>\n",
              "      <td>3.195642e-16</td>\n",
              "      <td>0.081081</td>\n",
              "      <td>0.360360</td>\n",
              "      <td>0.108108</td>\n",
              "      <td>0.117117</td>\n",
              "      <td>0.081081</td>\n",
              "      <td>0.045045</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>1.004535e+00</td>\n",
              "      <td>1.004535e+00</td>\n",
              "      <td>1.004535e+00</td>\n",
              "      <td>1.004535e+00</td>\n",
              "      <td>1.004535e+00</td>\n",
              "      <td>1.004535e+00</td>\n",
              "      <td>0.274198</td>\n",
              "      <td>0.482282</td>\n",
              "      <td>0.311925</td>\n",
              "      <td>0.323018</td>\n",
              "      <td>0.274198</td>\n",
              "      <td>0.208344</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>-1.056252e+00</td>\n",
              "      <td>-1.820693e+00</td>\n",
              "      <td>-1.815864e+00</td>\n",
              "      <td>-1.881881e+00</td>\n",
              "      <td>-1.727354e+00</td>\n",
              "      <td>-1.959270e+00</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>-7.468687e-01</td>\n",
              "      <td>-6.775778e-01</td>\n",
              "      <td>-6.661208e-01</td>\n",
              "      <td>-6.532226e-01</td>\n",
              "      <td>-7.161715e-01</td>\n",
              "      <td>-6.021914e-01</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>-3.347197e-01</td>\n",
              "      <td>-1.988371e-01</td>\n",
              "      <td>-1.642490e-01</td>\n",
              "      <td>-1.761149e-01</td>\n",
              "      <td>-2.562345e-01</td>\n",
              "      <td>-9.872365e-02</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>5.953272e-01</td>\n",
              "      <td>5.681250e-01</td>\n",
              "      <td>6.113711e-01</td>\n",
              "      <td>6.767680e-01</td>\n",
              "      <td>7.989702e-01</td>\n",
              "      <td>5.482232e-01</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>3.401737e+00</td>\n",
              "      <td>3.210969e+00</td>\n",
              "      <td>3.202855e+00</td>\n",
              "      <td>3.117195e+00</td>\n",
              "      <td>2.374535e+00</td>\n",
              "      <td>2.239206e+00</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "             Weight       Length1  ...       Smelt   Whitefish\n",
              "count  1.110000e+02  1.110000e+02  ...  111.000000  111.000000\n",
              "mean  -2.675537e-17  5.243553e-16  ...    0.081081    0.045045\n",
              "std    1.004535e+00  1.004535e+00  ...    0.274198    0.208344\n",
              "min   -1.056252e+00 -1.820693e+00  ...    0.000000    0.000000\n",
              "25%   -7.468687e-01 -6.775778e-01  ...    0.000000    0.000000\n",
              "50%   -3.347197e-01 -1.988371e-01  ...    0.000000    0.000000\n",
              "75%    5.953272e-01  5.681250e-01  ...    0.000000    0.000000\n",
              "max    3.401737e+00  3.210969e+00  ...    1.000000    1.000000\n",
              "\n",
              "[8 rows x 12 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xBfJZ76cFCXi",
        "outputId": "c6eb3dff-9f1c-4c6e-83bf-81f94cac7ce7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 598
        }
      },
      "source": [
        "# Correlation recheck\n",
        "\n",
        "plt.figure( figsize = [20,10])\n",
        "sns.heatmap( fish_train.corr(), annot = True, cmap = \"YlGnBu\")\n",
        "plt.show()"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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r3JVICIiIiIiIiJljcPYkgt5uZJWVZhojPEBvrTWDnVTTCIiIiIiIiJSRpQ4x4G1NtsYU98Y42etPemOoERERERERETKAs1xUMrJEYFdwBJjzGwg5a+d1tpRLolKRERERERERMqE0nYc7Mx9OXCuqiAiIiIiIiLi9RyeDqAMKO1yjK+4OhARERERERERKXtK1XFgjKkKPAW0AgL+2m+tvcxFcYmIiIiIiIh4nFZVKP2oi0nAFqAB8AqwB1jpophEREREREREpIwo7RwH4dbaz4wxj1prFwILjTHqOBARERERERGvplUVSt9xkJn738PGmH7AISDMNSGJiIiIiIiISFlR2o6D140xwcBwYAwQBDxemg/uSPT5H0M7v6gXq/Ry9IhRqdSunO3pEMqF6yPTPR1CufHBpiqeDqFciFo31NMhlBud2k7ydAjlwoaNQzwdQrmga6nSS8tSskrjRKbyJE46v5TQcWCMCQDuBxoDtYHPrLWXuiMwEREREREREfG8kiZHnAh0AjYAfYGRLo9IRERERERERMqMkh5VaGmtbQNgjPkMWOH6kERERERERETKhtIuRejNSsrBX5MiYq3NcnEsIiIiIiIiIlLGlDTioK0xJin33waomLttAGutDXJpdCIiIiIiIiIe5DCanf2MHQfWWi2JICIiIiIiInIeK+1yjCIiIiIiIiLnHS3HqHkeREREREREROQMNOJAREREREREpBi6264ciIiIiIiIiMgZaMSBiIiIiIiISDE0x4FGHIiIiIiIiIjIGWjEgYiIiIiIiEgxjLGeDsHjNOJARERERERERIqlEQciIiIiIiIixdAcBxpxICIiIiIiIiJnoBEHIiIiIiIiIsXQ3XblC5vRCAAAIABJREFUQERERERERETOwCtGHFhrmffRdLav3Iyvvy/XPjGUWo3rFip3aPt+ZoyaRNbJTJp0bknf+wZhjGHym18Qd/AYAOkn0gioUpEHxj7FztVb+PmLOWRnZuPj68MVdw6kYbum7q7eOWOt5YcJ09mWm6dBw4vO08Ht+5k+ahJZGZk07dySq+935um7N78g9kDBPD047imys7KZ+d5/ObTzADnZObTr3Zleg/u4u3rnlKva1Prfolgy7de8zx/dfYj7PniSmo3quK1urmKt5b8fzGDD8mj8/P2489mbqd+0cL2mf/IDS+dHkXoilXE/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tNY2ATDGfAOsdn5IIiIiIiIiIsWDpyoOLlpxkPHXE12iICIiIiIiInLpuVjFweXGmOTs5wbwy35tAGutDXRqdCIiIiIiIiJu5GHy3WDwknPBgQNrraerAhERERERERGR4ke3pBQRERERERGRQl3sUgURERERERGRS5Zux6iKAxERERERERG5AFUciIiIiIiIiBRCFQcuGDj45e4UZ39FqZBxp7+7Q5BSJkuTvxaR7jRbVK81T3J3CCVCbLqK+YpKB2JFM2fFve4OoUS4uc14d4dQYkxd1s/dIZQI2keJnKOKAxEREREREZFC6JSAciAiIiIiIiIiF6CKAxEREREREZFCGF22oooDERERERERESmcKg5ERERERERECqGCA1UciIiIiIiIiMgFqOJAREREREREpBCa40AVByIiIiIiIiJyAao4EBERERERESmEzrYrByIiIiIiIiIlnjEmxBgzzxizK/u/5Qto08wYs8IYs80Ys9kY06con62BAxEREREREZFCGGNd9vh/egFYYK2tCyzIfn2+VKCftbYR0AX4yBgTfLEP1sCBiIiIiIiISMnXExib/Xws0Ov8BtbandbaXdnPjwAxQPjFPlgDByIiIiIiIiIlXwVr7dHs58eAChdqbIy5CvAG9lzsgzU5ooiIiIiIiEghXHk3RmPMI8AjuRaNttaOzrV+PlCxgLcOyf3CWmvNBa59MMZUAsYD91lrsy4WlwYORERERERERIqB7EGC0RdYf31h64wxx40xlay1R7MHBmIKaRcI/AwMsdauLEpculRBREREREREpBDGuO7x/zQbuC/7+X3ArPzbYryBGcA4a+3Uon6wBg5ERERERERESr73gM7GmF3A9dmvMca0MMZ8nd2mN3ANcL8xZmP2o9nFPliXKoiIiIiIiIgUwpVzHPx/WGvjgU4FLF8LPJT9fAIw4X/97FI3cGCt5evhM1m3PAofX28GvtKXyxpUzdPmdPoZhr44jmOH4/Dw8KBl+0j6PX5TnjbL/9jM0BfH8sGYp6nTsJorN8ElrLV8N2Im67Pz9PgrfaldP3+ePhwyjuOH4vDw9ODKdpHcM8CRp+0b9jDmo1ns33OUp9+8hzbXXe6OzXCJ/2+u5ny/iAWzV+Hp6UFgsD8DhvQhvFKIOzbFZay1jBkxkw0rHDl77OWCczZiyDiOH87OWdtI7hpwUyGf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\n",
            "text/plain": [
              "<Figure size 1440x720 with 2 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FIg12uXGQKDt"
      },
      "source": [
        "# We can see a detailed view of correlations with low correlation too previously it was high with all"
      ],
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FknRnRzoFCcr"
      },
      "source": [
        "# Prepare dataframe for model building\n",
        "\n",
        "y_train = fish_train.pop('Weight')\n",
        "X_train = fish_train"
      ],
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nioF3DH8FCiJ",
        "outputId": "a7e4e35e-066d-4c76-f62d-16e548688184",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 565
        }
      },
      "source": [
        "# Import required library and create model one\n",
        "\n",
        "import statsmodels.api as sm\n",
        "\n",
        "X_train_lm = sm.add_constant(X_train)\n",
        "lr_1 = sm.OLS(y_train, X_train_lm).fit()\n",
        "lr_1.summary()"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<table class=\"simpletable\">\n",
              "<caption>OLS Regression Results</caption>\n",
              "<tr>\n",
              "  <th>Dep. Variable:</th>         <td>Weight</td>      <th>  R-squared:         </th> <td>   0.937</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.930</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   134.0</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Date:</th>             <td>Wed, 30 Sep 2020</td> <th>  Prob (F-statistic):</th> <td>2.75e-54</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Time:</th>                 <td>18:37:20</td>     <th>  Log-Likelihood:    </th> <td> -4.0254</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>No. Observations:</th>      <td>   111</td>      <th>  AIC:               </th> <td>   32.05</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Residuals:</th>          <td>    99</td>      <th>  BIC:               </th> <td>   64.57</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Model:</th>              <td>    11</td>      <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>const</th>     <td>   -0.0745</td> <td>    0.283</td> <td>   -0.264</td> <td> 0.793</td> <td>   -0.635</td> <td>    0.486</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length1</th>   <td>   -1.3094</td> <td>    1.233</td> <td>   -1.062</td> <td> 0.291</td> <td>   -3.755</td> <td>    1.136</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length2</th>   <td>    2.0792</td> <td>    1.600</td> <td>    1.300</td> <td> 0.197</td> <td>   -1.095</td> <td>    5.253</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length3</th>   <td>    0.5416</td> <td>    1.107</td> <td>    0.489</td> <td> 0.626</td> <td>   -1.656</td> <td>    2.739</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Height</th>    <td>   -0.0340</td> <td>    0.189</td> <td>   -0.180</td> <td> 0.858</td> <td>   -0.409</td> <td>    0.341</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Width</th>     <td>   -0.0339</td> <td>    0.127</td> <td>   -0.266</td> <td> 0.791</td> <td>   -0.286</td> <td>    0.219</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Parkki</th>    <td>    0.3025</td> <td>    0.239</td> <td>    1.264</td> <td> 0.209</td> <td>   -0.172</td> <td>    0.777</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Perch</th>     <td>    0.1544</td> <td>    0.396</td> <td>    0.389</td> <td> 0.698</td> <td>   -0.632</td> <td>    0.941</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Pike</th>      <td>   -0.9550</td> <td>    0.469</td> <td>   -2.037</td> <td> 0.044</td> <td>   -1.885</td> <td>   -0.025</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Roach</th>     <td>    0.1536</td> <td>    0.306</td> <td>    0.502</td> <td> 0.617</td> <td>   -0.454</td> <td>    0.761</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Smelt</th>     <td>    0.9505</td> <td>    0.405</td> <td>    2.348</td> <td> 0.021</td> <td>    0.147</td> <td>    1.754</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Whitefish</th> <td>    0.0569</td> <td>    0.313</td> <td>    0.182</td> <td> 0.856</td> <td>   -0.565</td> <td>    0.678</td>\n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "  <th>Omnibus:</th>       <td>31.147</td> <th>  Durbin-Watson:     </th> <td>   2.198</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  73.986</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Skew:</th>          <td> 1.054</td> <th>  Prob(JB):          </th> <td>8.59e-17</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Kurtosis:</th>      <td> 6.400</td> <th>  Cond. No.          </th> <td>    166.</td>\n",
              "</tr>\n",
              "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
            ],
            "text/plain": [
              "<class 'statsmodels.iolib.summary.Summary'>\n",
              "\"\"\"\n",
              "                            OLS Regression Results                            \n",
              "==============================================================================\n",
              "Dep. Variable:                 Weight   R-squared:                       0.937\n",
              "Model:                            OLS   Adj. R-squared:                  0.930\n",
              "Method:                 Least Squares   F-statistic:                     134.0\n",
              "Date:                Wed, 30 Sep 2020   Prob (F-statistic):           2.75e-54\n",
              "Time:                        18:37:20   Log-Likelihood:                -4.0254\n",
              "No. Observations:                 111   AIC:                             32.05\n",
              "Df Residuals:                      99   BIC:                             64.57\n",
              "Df Model:                          11                                         \n",
              "Covariance Type:            nonrobust                                         \n",
              "==============================================================================\n",
              "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
              "------------------------------------------------------------------------------\n",
              "const         -0.0745      0.283     -0.264      0.793      -0.635       0.486\n",
              "Length1       -1.3094      1.233     -1.062      0.291      -3.755       1.136\n",
              "Length2        2.0792      1.600      1.300      0.197      -1.095       5.253\n",
              "Length3        0.5416      1.107      0.489      0.626      -1.656       2.739\n",
              "Height        -0.0340      0.189     -0.180      0.858      -0.409       0.341\n",
              "Width         -0.0339      0.127     -0.266      0.791      -0.286       0.219\n",
              "Parkki         0.3025      0.239      1.264      0.209      -0.172       0.777\n",
              "Perch          0.1544      0.396      0.389      0.698      -0.632       0.941\n",
              "Pike          -0.9550      0.469     -2.037      0.044      -1.885      -0.025\n",
              "Roach          0.1536      0.306      0.502      0.617      -0.454       0.761\n",
              "Smelt          0.9505      0.405      2.348      0.021       0.147       1.754\n",
              "Whitefish      0.0569      0.313      0.182      0.856      -0.565       0.678\n",
              "==============================================================================\n",
              "Omnibus:                       31.147   Durbin-Watson:                   2.198\n",
              "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               73.986\n",
              "Skew:                           1.054   Prob(JB):                     8.59e-17\n",
              "Kurtosis:                       6.400   Cond. No.                         166.\n",
              "==============================================================================\n",
              "\n",
              "Warnings:\n",
              "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
              "\"\"\""
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6v9zRV3lFCnD"
      },
      "source": [
        "# Drop high p-value variable\n",
        "\n",
        "X_train.drop( \"Height\", axis = 1, inplace = True)"
      ],
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vJTC-8KuFCli",
        "outputId": "9bf37d18-aa9b-402a-a823-c267b31ba8d3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 547
        }
      },
      "source": [
        "# create model two after drop\n",
        "\n",
        "X_train_lm = sm.add_constant(X_train)\n",
        "lr_2 = sm.OLS(y_train, X_train_lm).fit()\n",
        "lr_2.summary()"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<table class=\"simpletable\">\n",
              "<caption>OLS Regression Results</caption>\n",
              "<tr>\n",
              "  <th>Dep. Variable:</th>         <td>Weight</td>      <th>  R-squared:         </th> <td>   0.937</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.931</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   148.8</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Date:</th>             <td>Wed, 30 Sep 2020</td> <th>  Prob (F-statistic):</th> <td>2.23e-55</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Time:</th>                 <td>18:37:20</td>     <th>  Log-Likelihood:    </th> <td> -4.0435</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>No. Observations:</th>      <td>   111</td>      <th>  AIC:               </th> <td>   30.09</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Residuals:</th>          <td>   100</td>      <th>  BIC:               </th> <td>   59.89</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Model:</th>              <td>    10</td>      <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>const</th>     <td>   -0.1082</td> <td>    0.211</td> <td>   -0.513</td> <td> 0.609</td> <td>   -0.527</td> <td>    0.311</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length1</th>   <td>   -1.3026</td> <td>    1.226</td> <td>   -1.062</td> <td> 0.291</td> <td>   -3.735</td> <td>    1.130</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length2</th>   <td>    2.0817</td> <td>    1.592</td> <td>    1.308</td> <td> 0.194</td> <td>   -1.077</td> <td>    5.240</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length3</th>   <td>    0.5203</td> <td>    1.096</td> <td>    0.475</td> <td> 0.636</td> <td>   -1.653</td> <td>    2.694</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Width</th>     <td>   -0.0476</td> <td>    0.102</td> <td>   -0.469</td> <td> 0.640</td> <td>   -0.249</td> <td>    0.154</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Parkki</th>    <td>    0.3165</td> <td>    0.225</td> <td>    1.405</td> <td> 0.163</td> <td>   -0.130</td> <td>    0.763</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Perch</th>     <td>    0.1970</td> <td>    0.316</td> <td>    0.623</td> <td> 0.535</td> <td>   -0.431</td> <td>    0.825</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Pike</th>      <td>   -0.8879</td> <td>    0.283</td> <td>   -3.142</td> <td> 0.002</td> <td>   -1.449</td> <td>   -0.327</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Roach</th>     <td>    0.1932</td> <td>    0.212</td> <td>    0.913</td> <td> 0.364</td> <td>   -0.227</td> <td>    0.613</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Smelt</th>     <td>    0.9953</td> <td>    0.318</td> <td>    3.133</td> <td> 0.002</td> <td>    0.365</td> <td>    1.625</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Whitefish</th> <td>    0.0929</td> <td>    0.240</td> <td>    0.387</td> <td> 0.699</td> <td>   -0.383</td> <td>    0.569</td>\n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "  <th>Omnibus:</th>       <td>31.337</td> <th>  Durbin-Watson:     </th> <td>   2.191</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  74.232</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Skew:</th>          <td> 1.062</td> <th>  Prob(JB):          </th> <td>7.60e-17</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Kurtosis:</th>      <td> 6.397</td> <th>  Cond. No.          </th> <td>    155.</td>\n",
              "</tr>\n",
              "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
            ],
            "text/plain": [
              "<class 'statsmodels.iolib.summary.Summary'>\n",
              "\"\"\"\n",
              "                            OLS Regression Results                            \n",
              "==============================================================================\n",
              "Dep. Variable:                 Weight   R-squared:                       0.937\n",
              "Model:                            OLS   Adj. R-squared:                  0.931\n",
              "Method:                 Least Squares   F-statistic:                     148.8\n",
              "Date:                Wed, 30 Sep 2020   Prob (F-statistic):           2.23e-55\n",
              "Time:                        18:37:20   Log-Likelihood:                -4.0435\n",
              "No. Observations:                 111   AIC:                             30.09\n",
              "Df Residuals:                     100   BIC:                             59.89\n",
              "Df Model:                          10                                         \n",
              "Covariance Type:            nonrobust                                         \n",
              "==============================================================================\n",
              "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
              "------------------------------------------------------------------------------\n",
              "const         -0.1082      0.211     -0.513      0.609      -0.527       0.311\n",
              "Length1       -1.3026      1.226     -1.062      0.291      -3.735       1.130\n",
              "Length2        2.0817      1.592      1.308      0.194      -1.077       5.240\n",
              "Length3        0.5203      1.096      0.475      0.636      -1.653       2.694\n",
              "Width         -0.0476      0.102     -0.469      0.640      -0.249       0.154\n",
              "Parkki         0.3165      0.225      1.405      0.163      -0.130       0.763\n",
              "Perch          0.1970      0.316      0.623      0.535      -0.431       0.825\n",
              "Pike          -0.8879      0.283     -3.142      0.002      -1.449      -0.327\n",
              "Roach          0.1932      0.212      0.913      0.364      -0.227       0.613\n",
              "Smelt          0.9953      0.318      3.133      0.002       0.365       1.625\n",
              "Whitefish      0.0929      0.240      0.387      0.699      -0.383       0.569\n",
              "==============================================================================\n",
              "Omnibus:                       31.337   Durbin-Watson:                   2.191\n",
              "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               74.232\n",
              "Skew:                           1.062   Prob(JB):                     7.60e-17\n",
              "Kurtosis:                       6.397   Cond. No.                         155.\n",
              "==============================================================================\n",
              "\n",
              "Warnings:\n",
              "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
              "\"\"\""
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Nx6s9g44FCgg"
      },
      "source": [
        "# Drop high p-value variable\n",
        "\n",
        "X_train.drop( \"Whitefish\", axis = 1, inplace = True)"
      ],
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "szBbHcd-FCa6",
        "outputId": "ab1992d0-422f-4e92-8b30-bc61fdbd1601",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 530
        }
      },
      "source": [
        "# create model three after drop\n",
        "\n",
        "X_train_lm = sm.add_constant(X_train)\n",
        "lr_3 = sm.OLS(y_train, X_train_lm).fit()\n",
        "lr_3.summary()"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<table class=\"simpletable\">\n",
              "<caption>OLS Regression Results</caption>\n",
              "<tr>\n",
              "  <th>Dep. Variable:</th>         <td>Weight</td>      <th>  R-squared:         </th> <td>   0.937</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.931</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   166.7</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Date:</th>             <td>Wed, 30 Sep 2020</td> <th>  Prob (F-statistic):</th> <td>1.80e-56</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Time:</th>                 <td>18:37:20</td>     <th>  Log-Likelihood:    </th> <td> -4.1267</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>No. Observations:</th>      <td>   111</td>      <th>  AIC:               </th> <td>   28.25</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Residuals:</th>          <td>   101</td>      <th>  BIC:               </th> <td>   55.35</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Model:</th>              <td>     9</td>      <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "     <td></td>        <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>const</th>   <td>   -0.0384</td> <td>    0.109</td> <td>   -0.351</td> <td> 0.726</td> <td>   -0.255</td> <td>    0.179</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length1</th> <td>   -1.2567</td> <td>    1.215</td> <td>   -1.034</td> <td> 0.304</td> <td>   -3.667</td> <td>    1.154</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length2</th> <td>    2.3667</td> <td>    1.406</td> <td>    1.684</td> <td> 0.095</td> <td>   -0.422</td> <td>    5.155</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length3</th> <td>    0.1677</td> <td>    0.607</td> <td>    0.276</td> <td> 0.783</td> <td>   -1.036</td> <td>    1.372</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Width</th>   <td>   -0.0363</td> <td>    0.097</td> <td>   -0.375</td> <td> 0.708</td> <td>   -0.229</td> <td>    0.156</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Parkki</th>  <td>    0.2490</td> <td>    0.142</td> <td>    1.751</td> <td> 0.083</td> <td>   -0.033</td> <td>    0.531</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Perch</th>   <td>    0.0920</td> <td>    0.162</td> <td>    0.567</td> <td> 0.572</td> <td>   -0.230</td> <td>    0.414</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Pike</th>    <td>   -0.9547</td> <td>    0.223</td> <td>   -4.284</td> <td> 0.000</td> <td>   -1.397</td> <td>   -0.513</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Roach</th>   <td>    0.1295</td> <td>    0.133</td> <td>    0.976</td> <td> 0.331</td> <td>   -0.134</td> <td>    0.393</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Smelt</th>   <td>    0.9015</td> <td>    0.205</td> <td>    4.407</td> <td> 0.000</td> <td>    0.496</td> <td>    1.307</td>\n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "  <th>Omnibus:</th>       <td>30.553</td> <th>  Durbin-Watson:     </th> <td>   2.208</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  71.794</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Skew:</th>          <td> 1.037</td> <th>  Prob(JB):          </th> <td>2.57e-16</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Kurtosis:</th>      <td> 6.350</td> <th>  Cond. No.          </th> <td>    144.</td>\n",
              "</tr>\n",
              "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
            ],
            "text/plain": [
              "<class 'statsmodels.iolib.summary.Summary'>\n",
              "\"\"\"\n",
              "                            OLS Regression Results                            \n",
              "==============================================================================\n",
              "Dep. Variable:                 Weight   R-squared:                       0.937\n",
              "Model:                            OLS   Adj. R-squared:                  0.931\n",
              "Method:                 Least Squares   F-statistic:                     166.7\n",
              "Date:                Wed, 30 Sep 2020   Prob (F-statistic):           1.80e-56\n",
              "Time:                        18:37:20   Log-Likelihood:                -4.1267\n",
              "No. Observations:                 111   AIC:                             28.25\n",
              "Df Residuals:                     101   BIC:                             55.35\n",
              "Df Model:                           9                                         \n",
              "Covariance Type:            nonrobust                                         \n",
              "==============================================================================\n",
              "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
              "------------------------------------------------------------------------------\n",
              "const         -0.0384      0.109     -0.351      0.726      -0.255       0.179\n",
              "Length1       -1.2567      1.215     -1.034      0.304      -3.667       1.154\n",
              "Length2        2.3667      1.406      1.684      0.095      -0.422       5.155\n",
              "Length3        0.1677      0.607      0.276      0.783      -1.036       1.372\n",
              "Width         -0.0363      0.097     -0.375      0.708      -0.229       0.156\n",
              "Parkki         0.2490      0.142      1.751      0.083      -0.033       0.531\n",
              "Perch          0.0920      0.162      0.567      0.572      -0.230       0.414\n",
              "Pike          -0.9547      0.223     -4.284      0.000      -1.397      -0.513\n",
              "Roach          0.1295      0.133      0.976      0.331      -0.134       0.393\n",
              "Smelt          0.9015      0.205      4.407      0.000       0.496       1.307\n",
              "==============================================================================\n",
              "Omnibus:                       30.553   Durbin-Watson:                   2.208\n",
              "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               71.794\n",
              "Skew:                           1.037   Prob(JB):                     2.57e-16\n",
              "Kurtosis:                       6.350   Cond. No.                         144.\n",
              "==============================================================================\n",
              "\n",
              "Warnings:\n",
              "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
              "\"\"\""
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Tr952UaQFCVG"
      },
      "source": [
        "# Drop high p-value variable\n",
        "\n",
        "X_train.drop( \"Length3\", axis = 1, inplace = True)"
      ],
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "md4MWVKmFCTn",
        "outputId": "bd1d9607-9d39-4043-ddba-feaf751e4269",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 512
        }
      },
      "source": [
        "# create model four after drop\n",
        "\n",
        "X_train_lm = sm.add_constant(X_train)\n",
        "lr_4 = sm.OLS(y_train, X_train_lm).fit()\n",
        "lr_4.summary()"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<table class=\"simpletable\">\n",
              "<caption>OLS Regression Results</caption>\n",
              "<tr>\n",
              "  <th>Dep. Variable:</th>         <td>Weight</td>      <th>  R-squared:         </th> <td>   0.937</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.932</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   189.3</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Date:</th>             <td>Wed, 30 Sep 2020</td> <th>  Prob (F-statistic):</th> <td>1.31e-57</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Time:</th>                 <td>18:37:20</td>     <th>  Log-Likelihood:    </th> <td> -4.1686</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>No. Observations:</th>      <td>   111</td>      <th>  AIC:               </th> <td>   26.34</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Residuals:</th>          <td>   102</td>      <th>  BIC:               </th> <td>   50.72</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Model:</th>              <td>     8</td>      <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "     <td></td>        <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>const</th>   <td>   -0.0147</td> <td>    0.068</td> <td>   -0.217</td> <td> 0.828</td> <td>   -0.149</td> <td>    0.120</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length1</th> <td>   -1.2905</td> <td>    1.204</td> <td>   -1.072</td> <td> 0.286</td> <td>   -3.678</td> <td>    1.097</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length2</th> <td>    2.5640</td> <td>    1.205</td> <td>    2.127</td> <td> 0.036</td> <td>    0.173</td> <td>    4.955</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Width</th>   <td>   -0.0350</td> <td>    0.096</td> <td>   -0.364</td> <td> 0.717</td> <td>   -0.226</td> <td>    0.156</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Parkki</th>  <td>    0.2279</td> <td>    0.119</td> <td>    1.908</td> <td> 0.059</td> <td>   -0.009</td> <td>    0.465</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Perch</th>   <td>    0.0528</td> <td>    0.078</td> <td>    0.677</td> <td> 0.500</td> <td>   -0.102</td> <td>    0.207</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Pike</th>    <td>   -0.9837</td> <td>    0.196</td> <td>   -5.022</td> <td> 0.000</td> <td>   -1.372</td> <td>   -0.595</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Roach</th>   <td>    0.1111</td> <td>    0.114</td> <td>    0.973</td> <td> 0.333</td> <td>   -0.115</td> <td>    0.338</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Smelt</th>   <td>    0.8703</td> <td>    0.170</td> <td>    5.124</td> <td> 0.000</td> <td>    0.533</td> <td>    1.207</td>\n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "  <th>Omnibus:</th>       <td>30.033</td> <th>  Durbin-Watson:     </th> <td>   2.198</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  70.244</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Skew:</th>          <td> 1.020</td> <th>  Prob(JB):          </th> <td>5.58e-16</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Kurtosis:</th>      <td> 6.321</td> <th>  Cond. No.          </th> <td>    116.</td>\n",
              "</tr>\n",
              "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
            ],
            "text/plain": [
              "<class 'statsmodels.iolib.summary.Summary'>\n",
              "\"\"\"\n",
              "                            OLS Regression Results                            \n",
              "==============================================================================\n",
              "Dep. Variable:                 Weight   R-squared:                       0.937\n",
              "Model:                            OLS   Adj. R-squared:                  0.932\n",
              "Method:                 Least Squares   F-statistic:                     189.3\n",
              "Date:                Wed, 30 Sep 2020   Prob (F-statistic):           1.31e-57\n",
              "Time:                        18:37:20   Log-Likelihood:                -4.1686\n",
              "No. Observations:                 111   AIC:                             26.34\n",
              "Df Residuals:                     102   BIC:                             50.72\n",
              "Df Model:                           8                                         \n",
              "Covariance Type:            nonrobust                                         \n",
              "==============================================================================\n",
              "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
              "------------------------------------------------------------------------------\n",
              "const         -0.0147      0.068     -0.217      0.828      -0.149       0.120\n",
              "Length1       -1.2905      1.204     -1.072      0.286      -3.678       1.097\n",
              "Length2        2.5640      1.205      2.127      0.036       0.173       4.955\n",
              "Width         -0.0350      0.096     -0.364      0.717      -0.226       0.156\n",
              "Parkki         0.2279      0.119      1.908      0.059      -0.009       0.465\n",
              "Perch          0.0528      0.078      0.677      0.500      -0.102       0.207\n",
              "Pike          -0.9837      0.196     -5.022      0.000      -1.372      -0.595\n",
              "Roach          0.1111      0.114      0.973      0.333      -0.115       0.338\n",
              "Smelt          0.8703      0.170      5.124      0.000       0.533       1.207\n",
              "==============================================================================\n",
              "Omnibus:                       30.033   Durbin-Watson:                   2.198\n",
              "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               70.244\n",
              "Skew:                           1.020   Prob(JB):                     5.58e-16\n",
              "Kurtosis:                       6.321   Cond. No.                         116.\n",
              "==============================================================================\n",
              "\n",
              "Warnings:\n",
              "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
              "\"\"\""
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jVhXeUUkFCNW"
      },
      "source": [
        "# Drop high p-value variable\n",
        "\n",
        "X_train.drop( \"Width\", axis = 1, inplace = True)"
      ],
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "g11MVOJ6JLUb",
        "outputId": "421cd562-c708-4145-9106-83593dfc5d31",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 494
        }
      },
      "source": [
        "# create model five after drop\n",
        "\n",
        "X_train_lm = sm.add_constant(X_train)\n",
        "lr_5 = sm.OLS(y_train, X_train_lm).fit()\n",
        "lr_5.summary()"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<table class=\"simpletable\">\n",
              "<caption>OLS Regression Results</caption>\n",
              "<tr>\n",
              "  <th>Dep. Variable:</th>         <td>Weight</td>      <th>  R-squared:         </th> <td>   0.937</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.933</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   218.1</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Date:</th>             <td>Wed, 30 Sep 2020</td> <th>  Prob (F-statistic):</th> <td>9.14e-59</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Time:</th>                 <td>18:37:20</td>     <th>  Log-Likelihood:    </th> <td> -4.2406</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>No. Observations:</th>      <td>   111</td>      <th>  AIC:               </th> <td>   24.48</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Residuals:</th>          <td>   103</td>      <th>  BIC:               </th> <td>   46.16</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Model:</th>              <td>     7</td>      <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "     <td></td>        <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>const</th>   <td>   -0.0216</td> <td>    0.065</td> <td>   -0.333</td> <td> 0.740</td> <td>   -0.150</td> <td>    0.107</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length1</th> <td>   -1.3465</td> <td>    1.189</td> <td>   -1.133</td> <td> 0.260</td> <td>   -3.704</td> <td>    1.011</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length2</th> <td>    2.5811</td> <td>    1.199</td> <td>    2.152</td> <td> 0.034</td> <td>    0.202</td> <td>    4.960</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Parkki</th>  <td>    0.2317</td> <td>    0.118</td> <td>    1.956</td> <td> 0.053</td> <td>   -0.003</td> <td>    0.467</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Perch</th>   <td>    0.0501</td> <td>    0.077</td> <td>    0.648</td> <td> 0.518</td> <td>   -0.103</td> <td>    0.203</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Pike</th>    <td>   -0.9273</td> <td>    0.119</td> <td>   -7.782</td> <td> 0.000</td> <td>   -1.164</td> <td>   -0.691</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Roach</th>   <td>    0.1122</td> <td>    0.114</td> <td>    0.987</td> <td> 0.326</td> <td>   -0.113</td> <td>    0.338</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Smelt</th>   <td>    0.8859</td> <td>    0.164</td> <td>    5.414</td> <td> 0.000</td> <td>    0.561</td> <td>    1.210</td>\n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "  <th>Omnibus:</th>       <td>31.314</td> <th>  Durbin-Watson:     </th> <td>   2.181</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  74.146</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Skew:</th>          <td> 1.061</td> <th>  Prob(JB):          </th> <td>7.93e-17</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Kurtosis:</th>      <td> 6.395</td> <th>  Cond. No.          </th> <td>    98.2</td>\n",
              "</tr>\n",
              "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
            ],
            "text/plain": [
              "<class 'statsmodels.iolib.summary.Summary'>\n",
              "\"\"\"\n",
              "                            OLS Regression Results                            \n",
              "==============================================================================\n",
              "Dep. Variable:                 Weight   R-squared:                       0.937\n",
              "Model:                            OLS   Adj. R-squared:                  0.933\n",
              "Method:                 Least Squares   F-statistic:                     218.1\n",
              "Date:                Wed, 30 Sep 2020   Prob (F-statistic):           9.14e-59\n",
              "Time:                        18:37:20   Log-Likelihood:                -4.2406\n",
              "No. Observations:                 111   AIC:                             24.48\n",
              "Df Residuals:                     103   BIC:                             46.16\n",
              "Df Model:                           7                                         \n",
              "Covariance Type:            nonrobust                                         \n",
              "==============================================================================\n",
              "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
              "------------------------------------------------------------------------------\n",
              "const         -0.0216      0.065     -0.333      0.740      -0.150       0.107\n",
              "Length1       -1.3465      1.189     -1.133      0.260      -3.704       1.011\n",
              "Length2        2.5811      1.199      2.152      0.034       0.202       4.960\n",
              "Parkki         0.2317      0.118      1.956      0.053      -0.003       0.467\n",
              "Perch          0.0501      0.077      0.648      0.518      -0.103       0.203\n",
              "Pike          -0.9273      0.119     -7.782      0.000      -1.164      -0.691\n",
              "Roach          0.1122      0.114      0.987      0.326      -0.113       0.338\n",
              "Smelt          0.8859      0.164      5.414      0.000       0.561       1.210\n",
              "==============================================================================\n",
              "Omnibus:                       31.314   Durbin-Watson:                   2.181\n",
              "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               74.146\n",
              "Skew:                           1.061   Prob(JB):                     7.93e-17\n",
              "Kurtosis:                       6.395   Cond. No.                         98.2\n",
              "==============================================================================\n",
              "\n",
              "Warnings:\n",
              "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
              "\"\"\""
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p36Z2EQcJLZf"
      },
      "source": [
        "# Drop high p-value variable\n",
        "\n",
        "X_train.drop( \"Perch\", axis = 1, inplace = True)"
      ],
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p_0MqhNKJLhi",
        "outputId": "4e904c2e-076d-4470-bf16-9006de555c0d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 476
        }
      },
      "source": [
        "# create model six after drop\n",
        "\n",
        "X_train_lm = sm.add_constant(X_train)\n",
        "lr_6 = sm.OLS(y_train, X_train_lm).fit()\n",
        "lr_6.summary()"
      ],
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<table class=\"simpletable\">\n",
              "<caption>OLS Regression Results</caption>\n",
              "<tr>\n",
              "  <th>Dep. Variable:</th>         <td>Weight</td>      <th>  R-squared:         </th> <td>   0.937</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.933</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   255.8</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Date:</th>             <td>Wed, 30 Sep 2020</td> <th>  Prob (F-statistic):</th> <td>6.74e-60</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Time:</th>                 <td>18:37:20</td>     <th>  Log-Likelihood:    </th> <td> -4.4664</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>No. Observations:</th>      <td>   111</td>      <th>  AIC:               </th> <td>   22.93</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Residuals:</th>          <td>   104</td>      <th>  BIC:               </th> <td>   41.90</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Model:</th>              <td>     6</td>      <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "     <td></td>        <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>const</th>   <td>    0.0139</td> <td>    0.035</td> <td>    0.400</td> <td> 0.690</td> <td>   -0.055</td> <td>    0.083</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length1</th> <td>   -0.9646</td> <td>    1.029</td> <td>   -0.937</td> <td> 0.351</td> <td>   -3.006</td> <td>    1.077</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length2</th> <td>    2.1894</td> <td>    1.033</td> <td>    2.119</td> <td> 0.036</td> <td>    0.141</td> <td>    4.238</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Parkki</th>  <td>    0.1893</td> <td>    0.098</td> <td>    1.923</td> <td> 0.057</td> <td>   -0.006</td> <td>    0.385</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Pike</th>    <td>   -0.9563</td> <td>    0.110</td> <td>   -8.683</td> <td> 0.000</td> <td>   -1.175</td> <td>   -0.738</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Roach</th>   <td>    0.0659</td> <td>    0.088</td> <td>    0.748</td> <td> 0.456</td> <td>   -0.109</td> <td>    0.241</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Smelt</th>   <td>    0.8195</td> <td>    0.127</td> <td>    6.439</td> <td> 0.000</td> <td>    0.567</td> <td>    1.072</td>\n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "  <th>Omnibus:</th>       <td>31.744</td> <th>  Durbin-Watson:     </th> <td>   2.224</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  76.099</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Skew:</th>          <td> 1.071</td> <th>  Prob(JB):          </th> <td>2.99e-17</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Kurtosis:</th>      <td> 6.444</td> <th>  Cond. No.          </th> <td>    84.8</td>\n",
              "</tr>\n",
              "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
            ],
            "text/plain": [
              "<class 'statsmodels.iolib.summary.Summary'>\n",
              "\"\"\"\n",
              "                            OLS Regression Results                            \n",
              "==============================================================================\n",
              "Dep. Variable:                 Weight   R-squared:                       0.937\n",
              "Model:                            OLS   Adj. R-squared:                  0.933\n",
              "Method:                 Least Squares   F-statistic:                     255.8\n",
              "Date:                Wed, 30 Sep 2020   Prob (F-statistic):           6.74e-60\n",
              "Time:                        18:37:20   Log-Likelihood:                -4.4664\n",
              "No. Observations:                 111   AIC:                             22.93\n",
              "Df Residuals:                     104   BIC:                             41.90\n",
              "Df Model:                           6                                         \n",
              "Covariance Type:            nonrobust                                         \n",
              "==============================================================================\n",
              "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
              "------------------------------------------------------------------------------\n",
              "const          0.0139      0.035      0.400      0.690      -0.055       0.083\n",
              "Length1       -0.9646      1.029     -0.937      0.351      -3.006       1.077\n",
              "Length2        2.1894      1.033      2.119      0.036       0.141       4.238\n",
              "Parkki         0.1893      0.098      1.923      0.057      -0.006       0.385\n",
              "Pike          -0.9563      0.110     -8.683      0.000      -1.175      -0.738\n",
              "Roach          0.0659      0.088      0.748      0.456      -0.109       0.241\n",
              "Smelt          0.8195      0.127      6.439      0.000       0.567       1.072\n",
              "==============================================================================\n",
              "Omnibus:                       31.744   Durbin-Watson:                   2.224\n",
              "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               76.099\n",
              "Skew:                           1.071   Prob(JB):                     2.99e-17\n",
              "Kurtosis:                       6.444   Cond. No.                         84.8\n",
              "==============================================================================\n",
              "\n",
              "Warnings:\n",
              "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
              "\"\"\""
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ReA0i8TpJLfm"
      },
      "source": [
        "# Drop high p-value variable\n",
        "\n",
        "X_train.drop( \"Roach\", axis = 1, inplace = True)"
      ],
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "L77eC-5MJLd1",
        "outputId": "776ea499-a699-45fa-dc80-9629d8b5f750",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 458
        }
      },
      "source": [
        "# create model seven after drop\n",
        "\n",
        "X_train_lm = sm.add_constant(X_train)\n",
        "lr_7 = sm.OLS(y_train, X_train_lm).fit()\n",
        "lr_7.summary()"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<table class=\"simpletable\">\n",
              "<caption>OLS Regression Results</caption>\n",
              "<tr>\n",
              "  <th>Dep. Variable:</th>         <td>Weight</td>      <th>  R-squared:         </th> <td>   0.936</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.933</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   308.2</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Date:</th>             <td>Wed, 30 Sep 2020</td> <th>  Prob (F-statistic):</th> <td>4.81e-61</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Time:</th>                 <td>18:37:20</td>     <th>  Log-Likelihood:    </th> <td> -4.7639</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>No. Observations:</th>      <td>   111</td>      <th>  AIC:               </th> <td>   21.53</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Residuals:</th>          <td>   105</td>      <th>  BIC:               </th> <td>   37.79</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Model:</th>              <td>     5</td>      <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "     <td></td>        <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>const</th>   <td>    0.0266</td> <td>    0.030</td> <td>    0.882</td> <td> 0.380</td> <td>   -0.033</td> <td>    0.086</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length1</th> <td>   -0.7083</td> <td>    0.969</td> <td>   -0.731</td> <td> 0.466</td> <td>   -2.629</td> <td>    1.212</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length2</th> <td>    1.9236</td> <td>    0.968</td> <td>    1.987</td> <td> 0.049</td> <td>    0.004</td> <td>    3.843</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Parkki</th>  <td>    0.1699</td> <td>    0.095</td> <td>    1.793</td> <td> 0.076</td> <td>   -0.018</td> <td>    0.358</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Pike</th>    <td>   -0.9596</td> <td>    0.110</td> <td>   -8.739</td> <td> 0.000</td> <td>   -1.177</td> <td>   -0.742</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Smelt</th>   <td>    0.7817</td> <td>    0.117</td> <td>    6.708</td> <td> 0.000</td> <td>    0.551</td> <td>    1.013</td>\n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "  <th>Omnibus:</th>       <td>28.606</td> <th>  Durbin-Watson:     </th> <td>   2.212</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  63.358</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Skew:</th>          <td> 0.992</td> <th>  Prob(JB):          </th> <td>1.75e-14</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Kurtosis:</th>      <td> 6.124</td> <th>  Cond. No.          </th> <td>    79.7</td>\n",
              "</tr>\n",
              "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
            ],
            "text/plain": [
              "<class 'statsmodels.iolib.summary.Summary'>\n",
              "\"\"\"\n",
              "                            OLS Regression Results                            \n",
              "==============================================================================\n",
              "Dep. Variable:                 Weight   R-squared:                       0.936\n",
              "Model:                            OLS   Adj. R-squared:                  0.933\n",
              "Method:                 Least Squares   F-statistic:                     308.2\n",
              "Date:                Wed, 30 Sep 2020   Prob (F-statistic):           4.81e-61\n",
              "Time:                        18:37:20   Log-Likelihood:                -4.7639\n",
              "No. Observations:                 111   AIC:                             21.53\n",
              "Df Residuals:                     105   BIC:                             37.79\n",
              "Df Model:                           5                                         \n",
              "Covariance Type:            nonrobust                                         \n",
              "==============================================================================\n",
              "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
              "------------------------------------------------------------------------------\n",
              "const          0.0266      0.030      0.882      0.380      -0.033       0.086\n",
              "Length1       -0.7083      0.969     -0.731      0.466      -2.629       1.212\n",
              "Length2        1.9236      0.968      1.987      0.049       0.004       3.843\n",
              "Parkki         0.1699      0.095      1.793      0.076      -0.018       0.358\n",
              "Pike          -0.9596      0.110     -8.739      0.000      -1.177      -0.742\n",
              "Smelt          0.7817      0.117      6.708      0.000       0.551       1.013\n",
              "==============================================================================\n",
              "Omnibus:                       28.606   Durbin-Watson:                   2.212\n",
              "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               63.358\n",
              "Skew:                           0.992   Prob(JB):                     1.75e-14\n",
              "Kurtosis:                       6.124   Cond. No.                         79.7\n",
              "==============================================================================\n",
              "\n",
              "Warnings:\n",
              "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
              "\"\"\""
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8cTaJ3uRJLXo"
      },
      "source": [
        "# Drop high p-value variable\n",
        "\n",
        "X_train.drop( \"Length1\", axis = 1, inplace = True)"
      ],
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9c98BQh3JLRw",
        "outputId": "294a8a00-ca12-44d8-cdd8-4d07103c26b4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 441
        }
      },
      "source": [
        "# create model eight after drop\n",
        "\n",
        "X_train_lm = sm.add_constant(X_train)\n",
        "lr_8 = sm.OLS(y_train, X_train_lm).fit()\n",
        "lr_8.summary()"
      ],
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<table class=\"simpletable\">\n",
              "<caption>OLS Regression Results</caption>\n",
              "<tr>\n",
              "  <th>Dep. Variable:</th>         <td>Weight</td>      <th>  R-squared:         </th> <td>   0.936</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.933</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   386.8</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Date:</th>             <td>Wed, 30 Sep 2020</td> <th>  Prob (F-statistic):</th> <td>2.99e-62</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Time:</th>                 <td>18:37:20</td>     <th>  Log-Likelihood:    </th> <td> -5.0459</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>No. Observations:</th>      <td>   111</td>      <th>  AIC:               </th> <td>   20.09</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Residuals:</th>          <td>   106</td>      <th>  BIC:               </th> <td>   33.64</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Model:</th>              <td>     4</td>      <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "     <td></td>        <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>const</th>   <td>    0.0330</td> <td>    0.029</td> <td>    1.144</td> <td> 0.255</td> <td>   -0.024</td> <td>    0.090</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length2</th> <td>    1.2163</td> <td>    0.037</td> <td>   33.257</td> <td> 0.000</td> <td>    1.144</td> <td>    1.289</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Parkki</th>  <td>    0.1634</td> <td>    0.094</td> <td>    1.736</td> <td> 0.086</td> <td>   -0.023</td> <td>    0.350</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Pike</th>    <td>   -0.9873</td> <td>    0.103</td> <td>   -9.603</td> <td> 0.000</td> <td>   -1.191</td> <td>   -0.784</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Smelt</th>   <td>    0.7466</td> <td>    0.106</td> <td>    7.047</td> <td> 0.000</td> <td>    0.537</td> <td>    0.957</td>\n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "  <th>Omnibus:</th>       <td>27.182</td> <th>  Durbin-Watson:     </th> <td>   2.219</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  59.797</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Skew:</th>          <td> 0.943</td> <th>  Prob(JB):          </th> <td>1.04e-13</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Kurtosis:</th>      <td> 6.062</td> <th>  Cond. No.          </th> <td>    5.14</td>\n",
              "</tr>\n",
              "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
            ],
            "text/plain": [
              "<class 'statsmodels.iolib.summary.Summary'>\n",
              "\"\"\"\n",
              "                            OLS Regression Results                            \n",
              "==============================================================================\n",
              "Dep. Variable:                 Weight   R-squared:                       0.936\n",
              "Model:                            OLS   Adj. R-squared:                  0.933\n",
              "Method:                 Least Squares   F-statistic:                     386.8\n",
              "Date:                Wed, 30 Sep 2020   Prob (F-statistic):           2.99e-62\n",
              "Time:                        18:37:20   Log-Likelihood:                -5.0459\n",
              "No. Observations:                 111   AIC:                             20.09\n",
              "Df Residuals:                     106   BIC:                             33.64\n",
              "Df Model:                           4                                         \n",
              "Covariance Type:            nonrobust                                         \n",
              "==============================================================================\n",
              "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
              "------------------------------------------------------------------------------\n",
              "const          0.0330      0.029      1.144      0.255      -0.024       0.090\n",
              "Length2        1.2163      0.037     33.257      0.000       1.144       1.289\n",
              "Parkki         0.1634      0.094      1.736      0.086      -0.023       0.350\n",
              "Pike          -0.9873      0.103     -9.603      0.000      -1.191      -0.784\n",
              "Smelt          0.7466      0.106      7.047      0.000       0.537       0.957\n",
              "==============================================================================\n",
              "Omnibus:                       27.182   Durbin-Watson:                   2.219\n",
              "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               59.797\n",
              "Skew:                           0.943   Prob(JB):                     1.04e-13\n",
              "Kurtosis:                       6.062   Cond. No.                         5.14\n",
              "==============================================================================\n",
              "\n",
              "Warnings:\n",
              "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
              "\"\"\""
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WIN_HF5_J1u-"
      },
      "source": [
        "# Drop high p-value variable\n",
        "\n",
        "X_train.drop( \"Parkki\", axis = 1, inplace = True)"
      ],
      "execution_count": 37,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dHgb7s3BJ1yc",
        "outputId": "968e4c24-1ed8-4390-bb70-9638a0086959",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        }
      },
      "source": [
        "# create model nine after drop\n",
        "\n",
        "X_train_lm = sm.add_constant(X_train)\n",
        "lr_9 = sm.OLS(y_train, X_train_lm).fit()\n",
        "lr_9.summary()"
      ],
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<table class=\"simpletable\">\n",
              "<caption>OLS Regression Results</caption>\n",
              "<tr>\n",
              "  <th>Dep. Variable:</th>         <td>Weight</td>      <th>  R-squared:         </th> <td>   0.934</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.932</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   505.2</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Date:</th>             <td>Wed, 30 Sep 2020</td> <th>  Prob (F-statistic):</th> <td>5.39e-63</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Time:</th>                 <td>18:37:20</td>     <th>  Log-Likelihood:    </th> <td> -6.6010</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>No. Observations:</th>      <td>   111</td>      <th>  AIC:               </th> <td>   21.20</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Residuals:</th>          <td>   107</td>      <th>  BIC:               </th> <td>   32.04</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Df Model:</th>              <td>     3</td>      <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "     <td></td>        <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
              "</tr>\n",
              "<tr>\n",
              "  <th>const</th>   <td>    0.0480</td> <td>    0.028</td> <td>    1.730</td> <td> 0.087</td> <td>   -0.007</td> <td>    0.103</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Length2</th> <td>    1.2001</td> <td>    0.036</td> <td>   33.621</td> <td> 0.000</td> <td>    1.129</td> <td>    1.271</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Pike</th>    <td>   -0.9741</td> <td>    0.103</td> <td>   -9.413</td> <td> 0.000</td> <td>   -1.179</td> <td>   -0.769</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Smelt</th>   <td>    0.7073</td> <td>    0.104</td> <td>    6.770</td> <td> 0.000</td> <td>    0.500</td> <td>    0.914</td>\n",
              "</tr>\n",
              "</table>\n",
              "<table class=\"simpletable\">\n",
              "<tr>\n",
              "  <th>Omnibus:</th>       <td>21.982</td> <th>  Durbin-Watson:     </th> <td>   2.230</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  40.375</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Skew:</th>          <td> 0.829</td> <th>  Prob(JB):          </th> <td>1.71e-09</td>\n",
              "</tr>\n",
              "<tr>\n",
              "  <th>Kurtosis:</th>      <td> 5.445</td> <th>  Cond. No.          </th> <td>    4.90</td>\n",
              "</tr>\n",
              "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."
            ],
            "text/plain": [
              "<class 'statsmodels.iolib.summary.Summary'>\n",
              "\"\"\"\n",
              "                            OLS Regression Results                            \n",
              "==============================================================================\n",
              "Dep. Variable:                 Weight   R-squared:                       0.934\n",
              "Model:                            OLS   Adj. R-squared:                  0.932\n",
              "Method:                 Least Squares   F-statistic:                     505.2\n",
              "Date:                Wed, 30 Sep 2020   Prob (F-statistic):           5.39e-63\n",
              "Time:                        18:37:20   Log-Likelihood:                -6.6010\n",
              "No. Observations:                 111   AIC:                             21.20\n",
              "Df Residuals:                     107   BIC:                             32.04\n",
              "Df Model:                           3                                         \n",
              "Covariance Type:            nonrobust                                         \n",
              "==============================================================================\n",
              "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
              "------------------------------------------------------------------------------\n",
              "const          0.0480      0.028      1.730      0.087      -0.007       0.103\n",
              "Length2        1.2001      0.036     33.621      0.000       1.129       1.271\n",
              "Pike          -0.9741      0.103     -9.413      0.000      -1.179      -0.769\n",
              "Smelt          0.7073      0.104      6.770      0.000       0.500       0.914\n",
              "==============================================================================\n",
              "Omnibus:                       21.982   Durbin-Watson:                   2.230\n",
              "Prob(Omnibus):                  0.000   Jarque-Bera (JB):               40.375\n",
              "Skew:                           0.829   Prob(JB):                     1.71e-09\n",
              "Kurtosis:                       5.445   Cond. No.                         4.90\n",
              "==============================================================================\n",
              "\n",
              "Warnings:\n",
              "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
              "\"\"\""
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aKU33HeSJ1sW"
      },
      "source": [
        "# Import required libraries\n",
        "from statsmodels.stats.outliers_influence import variance_inflation_factor"
      ],
      "execution_count": 39,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VClRb3wPKh0N",
        "outputId": "2f17ef48-3a03-4109-df75-b4852abdff54",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 137
        }
      },
      "source": [
        "# Create a dataframe that will contain the names of all the feature variables and their respective VIFs\n",
        "\n",
        "vif = pd.DataFrame()\n",
        "vif['Features'] = X_train.columns\n",
        "vif['VIF'] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]\n",
        "vif['VIF'] = round(vif['VIF'], 2)\n",
        "vif = vif.sort_values(by = \"VIF\", ascending = False)\n",
        "vif"
      ],
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Features</th>\n",
              "      <th>VIF</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Length2</td>\n",
              "      <td>2.04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Pike</td>\n",
              "      <td>1.67</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Smelt</td>\n",
              "      <td>1.37</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  Features   VIF\n",
              "0  Length2  2.04\n",
              "1     Pike  1.67\n",
              "2    Smelt  1.37"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KOgSnlmkKhyf"
      },
      "source": [
        "# Predict the target variable using final model\n",
        "\n",
        "y_train_weight = lr_9.predict(X_train_lm)"
      ],
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G6zyaVqPKhvr",
        "outputId": "75691d08-0fdb-40b0-e342-ada82ee14522",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 315
        }
      },
      "source": [
        "# Plot the histogram of the error terms\n",
        "\n",
        "fig = plt.figure()\n",
        "sns.distplot((y_train - y_train_weight), bins = 20)\n",
        "fig.suptitle('Error Terms', fontsize = 20)                  # Plot heading \n",
        "plt.xlabel('Errors', fontsize = 18)                         # X-label\n",
        "plt.show()"
      ],
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ha4Swj-FKhtC"
      },
      "source": [
        "# Prepare test dataframe"
      ],
      "execution_count": 43,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GY3FRVVbKhqg"
      },
      "source": [
        "# Scale previously scaled variables\n",
        "fish_test[num_vars] = scaler.transform(fish_test[num_vars])"
      ],
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i6iUOoRsKhoF",
        "outputId": "667559a7-45ef-4339-f486-93361435adcc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 287
        }
      },
      "source": [
        "# Statistical values check\n",
        "fish_test.describe()"
      ],
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Weight</th>\n",
              "      <th>Length1</th>\n",
              "      <th>Length2</th>\n",
              "      <th>Length3</th>\n",
              "      <th>Height</th>\n",
              "      <th>Width</th>\n",
              "      <th>Parkki</th>\n",
              "      <th>Perch</th>\n",
              "      <th>Pike</th>\n",
              "      <th>Roach</th>\n",
              "      <th>Smelt</th>\n",
              "      <th>Whitefish</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>48.000000</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>48.000000</td>\n",
              "      <td>48.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>0.025888</td>\n",
              "      <td>0.036259</td>\n",
              "      <td>0.034979</td>\n",
              "      <td>0.039569</td>\n",
              "      <td>0.098735</td>\n",
              "      <td>0.010812</td>\n",
              "      <td>0.041667</td>\n",
              "      <td>0.333333</td>\n",
              "      <td>0.104167</td>\n",
              "      <td>0.145833</td>\n",
              "      <td>0.104167</td>\n",
              "      <td>0.020833</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.897305</td>\n",
              "      <td>0.918729</td>\n",
              "      <td>0.922990</td>\n",
              "      <td>0.931927</td>\n",
              "      <td>1.125454</td>\n",
              "      <td>1.039884</td>\n",
              "      <td>0.201941</td>\n",
              "      <td>0.476393</td>\n",
              "      <td>0.308709</td>\n",
              "      <td>0.356674</td>\n",
              "      <td>0.308709</td>\n",
              "      <td>0.144338</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>-1.072250</td>\n",
              "      <td>-1.644829</td>\n",
              "      <td>-1.688114</td>\n",
              "      <td>-1.712993</td>\n",
              "      <td>-1.724831</td>\n",
              "      <td>-2.019783</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>-0.733311</td>\n",
              "      <td>-0.689791</td>\n",
              "      <td>-0.670683</td>\n",
              "      <td>-0.699667</td>\n",
              "      <td>-0.630789</td>\n",
              "      <td>-0.625814</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>-0.211346</td>\n",
              "      <td>0.196857</td>\n",
              "      <td>0.200749</td>\n",
              "      <td>0.279882</td>\n",
              "      <td>-0.270549</td>\n",
              "      <td>-0.058832</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>0.825805</td>\n",
              "      <td>0.758644</td>\n",
              "      <td>0.793870</td>\n",
              "      <td>0.845656</td>\n",
              "      <td>0.881678</td>\n",
              "      <td>0.957349</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>1.639257</td>\n",
              "      <td>1.823598</td>\n",
              "      <td>1.797614</td>\n",
              "      <td>1.698538</td>\n",
              "      <td>2.452560</td>\n",
              "      <td>1.911305</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "          Weight    Length1    Length2  ...      Roach      Smelt  Whitefish\n",
              "count  48.000000  48.000000  48.000000  ...  48.000000  48.000000  48.000000\n",
              "mean    0.025888   0.036259   0.034979  ...   0.145833   0.104167   0.020833\n",
              "std     0.897305   0.918729   0.922990  ...   0.356674   0.308709   0.144338\n",
              "min    -1.072250  -1.644829  -1.688114  ...   0.000000   0.000000   0.000000\n",
              "25%    -0.733311  -0.689791  -0.670683  ...   0.000000   0.000000   0.000000\n",
              "50%    -0.211346   0.196857   0.200749  ...   0.000000   0.000000   0.000000\n",
              "75%     0.825805   0.758644   0.793870  ...   0.000000   0.000000   0.000000\n",
              "max     1.639257   1.823598   1.797614  ...   1.000000   1.000000   1.000000\n",
              "\n",
              "[8 rows x 12 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2NggB7puKhle"
      },
      "source": [
        "# Prepare test dataset\n",
        "\n",
        "y_test = fish_test.pop('Weight')\n",
        "X_test = fish_test"
      ],
      "execution_count": 46,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "T4cuQ4KELl5E"
      },
      "source": [
        "# Adding constant variable to test dataframe\n",
        "\n",
        "X_test_m1 = sm.add_constant(X_test)"
      ],
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Lcq4hlL1LmI7"
      },
      "source": [
        "# Creating X_test_m1 dataframe by dropping variables from X_test_m1\n",
        "\n",
        "X_test_m1 = X_test_m1.drop([\"Height\", \"Whitefish\", \"Length3\", \"Width\", \"Perch\", \"Roach\", \"Length1\", \"Parkki\"], axis = 1)"
      ],
      "execution_count": 48,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XXr0_HUcLmGZ"
      },
      "source": [
        "# Making predictions using the ninth model\n",
        "\n",
        "y_pred_m1 = lr_9.predict(X_test_m1)"
      ],
      "execution_count": 49,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cBknDocULmD9",
        "outputId": "fe139623-3718-48e3-c4d8-9fffcf3be842",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 315
        }
      },
      "source": [
        "# Plotting y_test and y_pred to understand the spread\n",
        "\n",
        "fig = plt.figure()\n",
        "plt.scatter(y_test, y_pred_m1)\n",
        "fig.suptitle('y_test vs y_pred', fontsize = 20)              # Plot heading \n",
        "plt.xlabel('y_test', fontsize = 18)                          # X-label\n",
        "plt.ylabel('y_pred', fontsize = 16)  \n",
        "plt.show()"
      ],
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BEapspRXLmBZ",
        "outputId": "00aac21c-c7a6-49e9-8cb2-bffc8df6b469",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 483
        }
      },
      "source": [
        "# Check predicted vs actual target variable\n",
        "\n",
        "plt.figure( figsize = [10,8])\n",
        "n = range(1,len(y_test)+1)\n",
        "plt.plot(n, y_test, label = \"Actual\")\n",
        "plt.plot(n, y_pred_m1, label = \"Predicted\")\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "R7NfnqteLl-q",
        "outputId": "0da5957b-19e2-430f-9f8c-1088f88d68d9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# Checking R-square value of test dataset\n",
        "\n",
        "from sklearn.metrics import r2_score\n",
        "r2_score(y_test, y_pred_m1)"
      ],
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.9143237254054878"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 52
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cKm-NH3mJ1p4"
      },
      "source": [
        "# The equation of best fitted line is:\n",
        "\n",
        "# Weight = const * 0.0480 + Length2 *\t1.2001 + Smelt * 0.7073 + Pike * -0.9741"
      ],
      "execution_count": 53,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LfyIwW85J1nN"
      },
      "source": [
        ""
      ],
      "execution_count": 53,
      "outputs": []
    }
  ]
}