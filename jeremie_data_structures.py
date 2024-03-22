{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jnlandu/data_structures/blob/main/jeremie_data_structures.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Data structure"
      ],
      "metadata": {
        "id": "A_mDlw6sEB9e"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "A data structure is a way of organizing and storing data in our machine so that it can be accessed and used efficiently. It refers to the logical or mathematical representation of data, as well as the implementation in a computer program.\n",
        "\n"
      ],
      "metadata": {
        "id": "xHfgbNRtYrYt"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Data structures can be classified into two broad categories:\n",
        "\n",
        "\n",
        "*   **Linear Data Structure**: A data structure in which data elements are arranged sequentially or linearly, where each element is attached to its previous and next adjacent elements, is called a linear data structure. Examples are array, stack, queue, etc.\n",
        "*   **Non-linear Data Structure**: Data structures where data elements are not placed sequentially or linearly are called non-linear data structures. Examples are trees and graphs.\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "9egJAo-cYuad"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*mLRD8leEkOFY3A87akoaXQ.png)\n",
        "\n",
        "image credit:  https://python.plainenglish.io/understanding-python-data-structures-from-basics-to-advanced-7cf84212a373"
      ],
      "metadata": {
        "id": "JfDboB48aaKg"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "The non-primitive data structures can also be classified based on whether they are built-in or user-defined.\n",
        "\n",
        "1. Python offers implicit support for built in structures that include List, Tuple, Set and Dictionary.\n",
        "2. Users can also create their own data structures (like Stack, Tree, Queue, etc.) enabling them to have a full control over their functionality."
      ],
      "metadata": {
        "id": "BnoFGYTuc5Eg"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Need For Data Structure"
      ],
      "metadata": {
        "id": "0caGIsUOePz2"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "As the amount of data continues to grow, the applications become more and more complex, hence it becomes difficult for the programmer to manage this data as well as the software.\n",
        "\n",
        "Specifically, in machine learning algorithms which often require large volumes of data to effectively learn patterns, and relationships, and make accurate predictions or decisions.\n",
        "\n",
        "Typically, at any time, an application may face the following hurdles:\n",
        "*   **Searching Large amounts of Data**: Given the extensive processing and storage of data, our program may need to search specific data at any point. If the data isn't appropriately organized, retrieving the required information could be time-consuming due to its sheer volume. By employing efficient data structures for storage and organization, data retrieval becomes faster and more streamlined.\n",
        "*   **Speed of Processing**: Disorganized data may result in slow processing speed as a lot of time will be wasted in retrieving and accessing data.we organize data helps to stay concentrated on the processing of data to produce the desired output.\n",
        "*   **Multiple Simultaneous Requests**: Many applications these days need to make a simultaneous request to data. These requests should be processed efficiently for applications to run smoothly. Using a good data structure helps to minimize the concurrent requests turnaround time.\n",
        "\n",
        "References: https://www.softwaretestinghelp.com/data-structures-in-cpp/\n"
      ],
      "metadata": {
        "id": "P_TtXzFzfeDM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "While libraries like Pandas and NumPy provide powerful tools for data manipulation and analysis in machine learning, having a solid understanding of data structures remains essential for:\n",
        "\n",
        "*   Well understand how those libraries works and how the have been built\n",
        "*   Custom Implementations\n",
        "*   Optimization\n",
        "*   Algorithm Design\n",
        "*   Problem-Solving Skills\n",
        "*   etc.\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "y3bQUvMwjwOM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Array, List, Tuples, Set, Dictionnary"
      ],
      "metadata": {
        "id": "bA4OxyqwDoWt"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Declare a destroy_elements function that accepts two lists.\n",
        "It should return a list of all elements from the first list that are NOT contained in the second list.\n",
        " Use list comprehension in your solution.\n",
        "\n",
        " EXAMPLES\n",
        "* destroy_elements([1, 2, 3], [1, 2])      => [3]\n",
        "* destroy_elements([1, 2, 3], [1, 2, 3])   => []\n",
        "* destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]"
      ],
      "metadata": {
        "id": "RkKnSY9FnBkE"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "YwROkv2wnCvn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Given an array nums of size n, return the majority element.\n",
        "\n",
        "The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.\n",
        "\n",
        "Input: nums = [2,2,1,1,1,2,2] <br>\n",
        "Output: 2"
      ],
      "metadata": {
        "id": "ZvuUpvKNoFZi"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "g4-AqcKFoFzl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Suppose an array of length `n` sorted in ascending order is rotated between `1 and n times`. For example, the array `nums = [0,1,2,4,5,6,7]` might become:\n",
        "\n",
        "\n",
        "*   `[4,5,6,7,0,1,2] if it was rotated 4 times.`\n",
        "*   `[0,1,2,4,5,6,7] if it was rotated 7 times.`\n",
        "\n",
        "\n",
        "\n",
        "Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.\n",
        "\n",
        "Given the sorted rotated array nums of unique elements, return the minimum element of this array.\n",
        "\n",
        "Example:\n",
        "\n",
        "Input: nums = [3,4,5,1,2]   Output: 1\n",
        "\n",
        "Explanation: The original array was [1,2,3,4,5] rotated 3 times.\n",
        "\n",
        "Input: nums = [4,5,6,7,0,1,2]  Output: 0\n",
        "\n",
        "Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.\n",
        "\n",
        "Input: nums = [11,13,15,17]  Output: 11\n",
        "\n",
        "Explanation: The original array was [11,13,15,17] and it was rotated 4 times."
      ],
      "metadata": {
        "id": "gEHfH4d-mVvQ"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "itLlpNVb7dAo"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Given a list l, reverse l.\n",
        "\n",
        "Example= [1,2,3,4,5] ==> [5,4,3,2,1]. In this case the operation has to be done in-place. Do not allow new memory space</b>\n",
        "\n",
        "DON't USE THE PYTHON INDEXING [::-1]"
      ],
      "metadata": {
        "id": "9YhQql2NoNoo"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "JJKnBZphoOCz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.\n",
        "\n",
        "\n",
        "\n",
        "Example 1:\n",
        "\n",
        "Input: nums = [3,0,1]\n",
        "Output: 2\n",
        "Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.\n",
        "Example 2:\n",
        "\n",
        "Input: nums = [0,1]\n",
        "Output: 2\n",
        "Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.\n",
        "Example 3:\n",
        "\n",
        "Input: nums = [9,6,4,2,3,5,7,0,1]\n",
        "Output: 8\n",
        "Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.\n"
      ],
      "metadata": {
        "id": "sIOcVka_pKB5"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "IbNFcDWqpJML"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Given a string s, check whether s is a palindrome. s is the palindrome if s is equal to its reverse.Using:\n",
        "- slicing in python\n",
        "\n",
        "example : s='aba' is a palindrom\n",
        "s='abaa' isnot a palindrom"
      ],
      "metadata": {
        "id": "jWkw5jP5o4ZA"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "BjWQX-xGpKgf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Given a list, dictionary, and a Key K, print the value of K from the dictionary if the key is present in both, the list and the dictionary.\n",
        "\n",
        "Use a try-except block to handle the KeyError that may occur if K is not present in test_dict.\n",
        "\n",
        "\n",
        "Input : `test_list = [\"Gfg\", \"is\", \"Good\", \"for\", \"Geeks\"]`,\n",
        "                `test_dict = {\"Gfg\" : 5, \"Best\" : 6}, K = \"Gfg\"`\n",
        "\n",
        "Output : 5\n",
        "\n",
        "Explanation : \"Gfg\" is present in list and has value 5 in dictionary.\n",
        "\n",
        "\n",
        "Input : `test_list = [\"Good\", \"for\", \"Geeks\"]`,\n",
        "                `test_dict = {\"Gfg\" : 5, \"Best\" : 6}` `, K = \"Gfg\"`\n",
        "\n",
        "Output : None\n",
        "\n",
        "Explanation : \"Gfg\" not present in List.\n"
      ],
      "metadata": {
        "id": "VYb2zHDorcb6"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "BIN4m_igrdTJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Stack"
      ],
      "metadata": {
        "id": "4lViF_B_DwAG"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Stack is a linear data structure that follows the principle of LIFO (Last In First Out) to store data.\n",
        "\n",
        "![](https://media.geeksforgeeks.org/wp-content/uploads/20220714004311/Stack-660x566.png)\n",
        "\n",
        "image credit:  https://media.geeksforgeeks.org/wp-content/uploads/20220714004311/Stack-660x566.png"
      ],
      "metadata": {
        "id": "tHaXpuuBKYuS"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Basic operations on stack"
      ],
      "metadata": {
        "id": "kq-r8WbqKfoq"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Some basic operations allow us to perform different actions on a stack.\n",
        "\n",
        "*   push() to insert an element into the stack\n",
        "*   pop() to remove an element from the stack\n",
        "*   top() Returns the top element of the stack.\n",
        "*   isEmpty() returns true if the stack is empty else false.\n",
        "*   size() returns the size of the stack.\n",
        "\n",
        "In python, stacks can be implented using lists"
      ],
      "metadata": {
        "id": "_HUfpnNIKpAk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Stack():\n",
        "\n",
        "  def __init__(self):\n",
        "    self.stack = []\n",
        "\n",
        "  def get_length(self):\n",
        "\n",
        "    return len(self.stack)\n",
        "\n",
        "  def isEmpty(self):\n",
        "    if len(self.stack) != 0:\n",
        "      return False\n",
        "    else:\n",
        "      return True\n",
        "\n",
        "  def push(self, x):\n",
        "    self.stack.append(x)\n",
        "\n",
        "  def pop(self):\n",
        "    if not self.isEmpty():\n",
        "      last = self.stack[-1]\n",
        "      self.stack = self.stack[:len(self.stack)-1]\n",
        "      print(last)\n",
        "    else:\n",
        "      pass\n",
        "  def top(self):\n",
        "    return self.Stack[-1]\n",
        "\n",
        "  def display_stack(self):\n",
        "    self.stack = self.stack[::-1]\n",
        "    return self.stack"
      ],
      "metadata": {
        "id": "CeLwIsW3KHob"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "my_stack = Stack()\n",
        "my_stack.push(4)\n",
        "my_stack.push(5)\n",
        "my_stack.push(3)\n",
        "my_stack.push(7)\n",
        "my_stack.pop()\n",
        "\n",
        "print(my_stack.display_stack())\n",
        "\n",
        "ls = my_stack.stack #.reverse()\n",
        "print(ls)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fBYVDpUDLtk9",
        "outputId": "97e05702-5833-4620-a7d6-c29d79c080ef"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7\n",
            "[4, 5, 3]\n",
            "[4, 5, 3]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "new = Stack()\n",
        "new.push('[') #, )\n",
        "new.display_stack()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P1ut4pdfV1K-",
        "outputId": "4d0de7a7-527b-407b-b73d-0a96f1173136"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['[']"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st = '[()]{}{()()}'\n",
        "len(st)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wP5DveawXF3U",
        "outputId": "28675af7-dea0-4d25-8953-d41f09afcf94"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "12"
            ]
          },
          "metadata": {},
          "execution_count": 83
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Some applications"
      ],
      "metadata": {
        "id": "viddoJYUNmZ4"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "\n",
        "Given a string s, write a function reverseString that returns the reversed string of s using stack\n",
        "\n",
        "Input: abc\n",
        "\n",
        "output: cba\n",
        "\n",
        "Input: abc def\n",
        "\n",
        "\n",
        "output: fed cba"
      ],
      "metadata": {
        "id": "OIh0o7uk_84V"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M_8dVUjLb9R6",
        "outputId": "fff20d3a-ab23-43a7-8298-7e0a897e59fb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.0009765625"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def reverse(my_string):\n",
        "  stack, st = Stack(), str()\n",
        "  for i in my_string:\n",
        "    stack.push(i)\n",
        "  for i in stack.display_stack():\n",
        "    st +=  i\n",
        "  return st\n"
      ],
      "metadata": {
        "id": "Y6Ph0tZMNhDw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "reverse(\"abc\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "5zsFd2d_STpa",
        "outputId": "2366e88b-2ac7-4a9f-beda-b6cfdcb8a78e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'cba'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 66
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Check for Balanced Brackets in an expression (well-formedness)\n",
        "\n",
        "\n",
        "Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.\n",
        "\n",
        "Example:\n",
        "\n",
        "Input: exp = “[()]{}{[()()]()}”\n",
        "Output: Balanced\n",
        "Explanation: all the brackets are well-formed\n",
        "\n",
        "Input: exp = “[(])”\n",
        "Output: Not Balanced\n",
        "Explanation: 1 and 4 brackets are not balanced because\n",
        "there is a closing ‘]’ before the closing ‘(‘\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "MbU9O7SwRHno"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def are_brackets_balanced(s):\n",
        "  lfs = [\"{\",\"(\", \"[\"]\n",
        "  stack = Stack()\n",
        "  for  x in s:\n",
        "    stack.push(x)\n",
        "    if"
      ],
      "metadata": {
        "id": "oK8I-ZXHNhSz",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 105
        },
        "outputId": "a7b5920e-b0a1-4f89-9466-5b68cf6e84d4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-10-e65f4c1faecb>, line 6)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-10-e65f4c1faecb>\"\u001b[0;36m, line \u001b[0;32m6\u001b[0m\n\u001b[0;31m    if\u001b[0m\n\u001b[0m      ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x8-QUBHEbSPZ",
        "outputId": "a189c0c2-18c9-48ca-e712-9a014716e164"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<__main__.Stack at 0x7c3bfb2a9630>"
            ]
          },
          "metadata": {},
          "execution_count": 89
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Queue"
      ],
      "metadata": {
        "id": "8aqpCVDeDybi"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Same as Stack, Queue is also a linear data structure. However Queue store data in a FIFO(FIrst In First Out) manner\n",
        "\n",
        "![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/02/Queue.png)\n",
        "\n",
        "\n",
        "image credit: https://www.geeksforgeeks.org/python-data-structures-and-algorithms/\n",
        "\n"
      ],
      "metadata": {
        "id": "yQW3eR92VUg5"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Basics operations of Queue\n",
        "\n",
        "\n",
        "*   Enqueue() Adds (or stores) an element to the end of the queue.\n",
        "*   Dequeue() Removal of elements from the queue.\n",
        "*   Peek() or front() Acquires the data element available at the front node of the queue without deleting it.\n",
        "*   rear() This operation returns the element at the rear end without removing it.\n",
        "*   isFull() Validates if the queue is full.\n",
        "*   isNull() Checks if the queue is empty."
      ],
      "metadata": {
        "id": "Ge-8GbXARNK0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Queue:\n",
        "  \"Write your code here\"\n",
        "\n",
        "  def __init__(self, max_size = None):\n",
        "    self.queue = []\n",
        "    self.size = max_size\n",
        "\n",
        "  def enqueue(self,x):\n",
        "    self.queue.append(x)\n",
        "  def dequeue(self):\n",
        "    if not self.isNull():\n",
        "      self.queue = self.queue[1:len(self.queue)-1]\n",
        "    else:\n",
        "      print(\"Empty queue\")\n",
        "  def front(self):\n",
        "    return self.queue[0]\n",
        "\n",
        "  def front(self):\n",
        "    return self.queue[0]\n",
        "  def isNull(self):\n",
        "    if self.queue == []:\n",
        "      return True\n",
        "    else:\n",
        "      return False\n",
        "\n",
        "  def roar(self):  # for roar\n",
        "     return self.queue[:-1]\n",
        "  def display_queue(self):\n",
        "    print(self.queue)\n",
        "\n",
        "  def is_full(self):\n",
        "    pass"
      ],
      "metadata": {
        "id": "_u2lE_feDzwt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "my_queue = Queue(max_size=5)\n",
        "my_queue.enqueue(1)\n",
        "my_queue.enqueue(-1)\n",
        "my_queue.enqueue(3)\n",
        "my_queue.enqueue(0)\n",
        "my_queue.enqueue(10)\n",
        "my_queue.enqueue(6)\n",
        "my_queue.display_queue()\n",
        "print(my_queue.dequeue())\n",
        "#print(my_queue.peek())\n",
        "print(my_queue.roar())\n",
        "#print(my_queue.is_full())\n",
        "print(my_queue.isNull())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XIuQe8QLyH_0",
        "outputId": "21558efb-8788-49c2-c33e-53b69f74056b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, -1, 3, 0, 10, 6]\n",
            "None\n",
            "[-1, 3, 0]\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ls = [1,2,2,28,3, 0, 2]\n",
        "ls.remove(2)\n",
        "ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-QsRPcaSut5N",
        "outputId": "e93af37b-818d-49a0-d9cb-3150f733f148"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 2, 28, 3, 0, 2]"
            ]
          },
          "metadata": {},
          "execution_count": 135
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "pPjsHtYdzlaE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Queues and Stacks have  two conditions that need to be checked:\n",
        "\n",
        "*  overflow → insertion into a queue or stack that is full\n",
        "*   underflow → deletion from an empty queue or stack"
      ],
      "metadata": {
        "id": "6_aPGsSQaznf"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Some applications: Priority Queue"
      ],
      "metadata": {
        "id": "158eDe1eO6Ww"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "`**A priority queue**` is a special type of queue in which each element is associated with a priority and is served according to its priority. There are two types of Priority Queues. They are:\n",
        "\n",
        "\n",
        "\n",
        "*   Ascending Priority Queue: Element can be inserted arbitrarily but only smallest element can be removed.\n",
        "*   Descending priority Queue: Element can be inserted arbitrarily but only the largest element can be removed first from the given Queue.\n"
      ],
      "metadata": {
        "id": "e1bzOMF5z9st"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Rewrite the function dequeue for ascending priority; You can use try/catch block by raising an IndexError when the queue is empty."
      ],
      "metadata": {
        "id": "3yVKigCV0kG0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Queue:\n",
        "  \"Write your code here\"\n",
        "\n",
        "  def __init__(self, max_size = None):\n",
        "    self.queue = []\n",
        "    self.size = max_size\n",
        "    self.min = None\n",
        "\n",
        "  def enqueue(self,x):\n",
        "    self.queue.append(x)\n",
        "\n",
        "  def dequeue(self):\n",
        "    if not self.isNull():\n",
        "      self.queue = self.queue[:len(self.queue)-1]\n",
        "    else:\n",
        "      print(\"Empty queue\")\n",
        "  def rear(self):\n",
        "    return self.queue[1]\n",
        "  def front(self):\n",
        "    return self.queue[0]\n",
        "  def isNull(self):\n",
        "    if self.queue == []:\n",
        "      return True\n",
        "    else:\n",
        "      return False\n",
        "\n",
        "  def peek(self):\n",
        "    return self.queue[:-1]\n",
        "  def display_queue(self):\n",
        "    print(self.queue)\n",
        "\n",
        "  def dequeue_asc(self):\n",
        "    if not self.isNull():\n",
        "       self.queue.remove(min(self.queue))\n",
        "    else:\n",
        "      print(\"Empty queue\")"
      ],
      "metadata": {
        "id": "ShS62ahCPAQb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "my_queue = Queue(max_size=5)\n",
        "my_queue.enqueue(1)\n",
        "my_queue.enqueue(-1)\n",
        "my_queue.enqueue(3)\n",
        "my_queue.enqueue(0)\n",
        "my_queue.enqueue(10)\n",
        "my_queue.enqueue(6)\n",
        "my_queue.display_queue()\n",
        "print(my_queue.dequeue())\n",
        "print(my_queue.peek())\n",
        "print(my_queue.rear())\n",
        "#print(my_queue.is_full())\n",
        "print(my_queue.isNull())\n"
      ],
      "metadata": {
        "id": "D2aJXEgD1z3t",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a3895bc1-2eee-45a7-d239-4fc81413f439"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, -1, 3, 0, 10, 6]\n",
            "None\n",
            "[1, -1, 3, 0]\n",
            "-1\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Linked List"
      ],
      "metadata": {
        "id": "zde5OxGgDsdY"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "A linked list is a linear data structure that includes a series of connected nodes that are not stored at contiguous memory location.\n",
        "\n",
        "It is represented by a pointer to the first node of the linked list. The first node is called the **head**. If the linked list is empty, then the value of the head is **NULL**. Each node in a list consists of at least two parts:\n",
        "\n",
        "* Data\n",
        "* Pointer (Or Reference) to the next node\n",
        "\n",
        "![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist.png)\n",
        "\n",
        "\n",
        "https://realpython.com/linked-lists-python/"
      ],
      "metadata": {
        "id": "zvyd4mVZPJbe"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Basic operations\n",
        "\n",
        "\n",
        "\n",
        "*   Insert: we can insert at the Beginning, Insert at the End, Insert at a Specific Position\n",
        "*   Delete: we can delete from the Beginning, from the End, at a Specific Position\n",
        "*   Display: disply by traversing the linked list from the head to the end, visiting each node in turn.\n",
        "*   Search: look for a node with a specific value or property.\n",
        "*   Get Length: count the number of nodes.\n",
        "*   Access: Access data in a specific node by traversing the list or directly indexing if the list supports it.\n",
        "*   Update: update the data in a specific node by traversing the list to find it and modifying its data.\n",
        "*   Concatenate: Concatenate two linked lists by making the last node of the first list point to the head of the second list.\n",
        "*   Reverse: Reverse the order of nodes in the linked list.\n",
        "*   Sort: Sort the linked list by rearranging nodes according to a specific criterion, such as value or property.\n",
        "\n"
      ],
      "metadata": {
        "id": "IXOU8UvrRWbx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "    def __init__(self, data):\n",
        "      self.node = data\n",
        "      self.next = None\n",
        "\n",
        "\n",
        "\n",
        "class LinkedList:\n",
        "\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "\n",
        "    def insertAtBeginning(self, item):\n",
        "      var = Node(item)\n",
        "      if self.head == None:\n",
        "        self.head = var\n",
        "      else:\n",
        "        var.next = self.head\n",
        "        self.head = var\n",
        "\n",
        "    def insertAfter(self, item, index):\n",
        "      newNode = Node(item)\n",
        "      current = self.head\n",
        "      flag = False\n",
        "      if index == 0:\n",
        "        self.insertAtBeginning(item)\n",
        "      else:\n",
        "        count = 0\n",
        "        while count != index and current != None : # or current != None:\n",
        "          current = current.next\n",
        "          count += 1\n",
        "        if current == None:\n",
        "          print(\"Position not found\")\n",
        "        else:\n",
        "          newNode.next = current.next\n",
        "          current.next = newNode\n",
        "\n",
        "\n",
        "        #var = Node(item)\n",
        "        #previous_node.next = var\n",
        "        #var.next = previous_node\n",
        "        #previous_node = var\n",
        "\n",
        "    def insertAtEnd(self, item):\n",
        "      var = Node(item)\n",
        "      if self.head == None:\n",
        "        self.head = var\n",
        "      else:\n",
        "        current = self.head\n",
        "        while current.next != None:\n",
        "          current = current.next\n",
        "        current.next =  var\n",
        "\n",
        "    def deleteItem(self, item):\n",
        "      if self.head == None:\n",
        "        return \"Empty queue\"\n",
        "      else:\n",
        "        if self.head.node == item:\n",
        "          self.head = self.head.next\n",
        "        else:\n",
        "          current = self.head\n",
        "          while current != None and current.next.node != item:\n",
        "            current = current.next\n",
        "          if current == None:\n",
        "            return \"Item not found\"\n",
        "          else:\n",
        "            current.next = current.next.next\n",
        "\n",
        "    def display(self):\n",
        "      current = self.head\n",
        "      while current.next != None:\n",
        "        print(current.node, end='-->')\n",
        "        current = current.next\n",
        "      print(current.node)\n",
        "\n",
        "    def search(self, item):\n",
        "      current = self.head\n",
        "      if self.head.node == item:\n",
        "        return True\n",
        "      else:\n",
        "        while current != None:\n",
        "          if current.node == item:\n",
        "            return True\n",
        "          else:\n",
        "            current = current.next\n",
        "        return False\n",
        "\n",
        "    def get_length(self):\n",
        "        current, count = self.head, 0\n",
        "        if self.head == None:\n",
        "          return 0\n",
        "        else:\n",
        "          while current != None:\n",
        "            count += 1\n",
        "            current = current.next\n",
        "          return count\n",
        "\n",
        "    def access(self, index):\n",
        "      current = self.head\n",
        "      if index == 0:\n",
        "        return current.node\n",
        "      else:\n",
        "        count = 0\n",
        "        while count != index and current != None : # or current != None:\n",
        "          current = current.next\n",
        "          count += 1\n",
        "        if current == None:\n",
        "          print(\"Position not found\")\n",
        "        else:\n",
        "          return current.node\n",
        "\n",
        "    def update(self, index, new_data):\n",
        "      current, count = self.head, 0\n",
        "      if current == None:\n",
        "        return \"Empty queue\"\n",
        "      else:\n",
        "        while count != index and current != None:\n",
        "          current = current.next\n",
        "          count +=1\n",
        "        if current == None:\n",
        "          print(\"Out of range\")\n",
        "        else:\n",
        "          current.node = new_data\n"
      ],
      "metadata": {
        "id": "p7TTDb25Dvc2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "linked_list = LinkedList()\n",
        "#display(linked_list)\n",
        "linked_list.insertAtBeginning(2)\n",
        "linked_list.insertAtBeginning(9)\n",
        "linked_list.insertAtEnd(8)\n",
        "linked_list.insertAfter(7,1)\n",
        "linked_list.insertAfter(0,1)\n",
        "linked_list.display()\n",
        "print(linked_list.get_length())\n",
        "linked_list.search(10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kPivLrrbUZDO",
        "outputId": "1276d102-f8ea-4149-e3b8-31127c68eeaf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "9-->2-->0-->7-->8\n",
            "5\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "linked_list.update(1, 1)\n",
        "linked_list.display()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 156
        },
        "id": "ZI4cyTlx3LhZ",
        "outputId": "d8c7785e-f793-491b-d6b2-c66d6ee9a190"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'linked_list' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-9-e6ff2c498cdb>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mlinked_list\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mlinked_list\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdisplay\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'linked_list' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "linked_list.access(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-ejt6wTW62oh",
        "outputId": "58ec35fb-d381-4cd3-e8db-414f9272ed3c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Position not found\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Vv9IZmtp62lB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "linked_list = LinkedList()\n",
        "\n",
        "#display(linked_list)\n",
        "linked_list.insertAtBeginning(2)\n",
        "linked_list.display()\n",
        "\n",
        "linked_list.insertAtEnd(4)\n",
        "linked_list.display()\n",
        "\n",
        "linked_list.insertAtBeginning(5)\n",
        "linked_list.display()\n",
        "\n",
        "linked_list.insertAtEnd(6)\n",
        "linked_list.display()\n",
        "\n",
        "linked_list.insertAtEnd(7)\n",
        "linked_list.display()\n",
        "\n",
        "#linked_list.insertAfter(3,linked_list.head.next)\n",
        "linked_list.display()\n",
        "\n",
        "#linked_list.insertAfter(7,linked_list.head.next)\n",
        "#linked_list.display()\n",
        "\n",
        "#linked_list.deleteItem(1)\n",
        "#linked_list.display()\n",
        "\n",
        "#linked_list.update(3, 10)\n",
        "#linked_list.display()\n",
        "#linked_list.update(20, 1)\n",
        "#linked_list.display()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EVdpp9p0PR9Y",
        "outputId": "0005ce67-c1c0-45db-8f16-f3b3d66a8715"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "2-->4\n",
            "5-->2-->4\n",
            "5-->2-->4-->6\n",
            "5-->2-->4-->6-->7\n",
            "5-->2-->4-->6-->7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Exercises"
      ],
      "metadata": {
        "id": "YkzwOpmgRfKx"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercises\n",
        "\n",
        "Write the function concatenate to concatenate two linked list\n",
        "\n",
        "Example:\n",
        "\n",
        "Input\n",
        "\n",
        "`first_list = 5 -> 2 -> 7 -> 10 -> `\n",
        "\n",
        "`second_list = 4 -> 6 -> 7 -> `\n",
        "\n",
        "output\n",
        "\n",
        "`reverse_list = 5 -> 2 -> 7 -> 10 -> 4 -> 6 -> 7 -> `"
      ],
      "metadata": {
        "id": "-dQV-U6360VE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "    def __init__(self, data):\n",
        "      self.node = data\n",
        "      self.next = None\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "class LinkedList:\n",
        "\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "\n",
        "    def insertAtBeginning(self, item):\n",
        "      var = Node(item)\n",
        "      if self.head == None:\n",
        "        self.head = var\n",
        "      else:\n",
        "        var.next = self.head\n",
        "        self.head = var\n",
        "\n",
        "    def insertAfter(self, item, index):\n",
        "      newNode = Node(item)\n",
        "      current = self.head\n",
        "      flag = False\n",
        "      if index == 0:\n",
        "        self.insertAtBeginning(item)\n",
        "      else:\n",
        "        count = 0\n",
        "        while count != index and current != None : # or current != None:\n",
        "          current = current.next\n",
        "          count += 1\n",
        "        if current == None:\n",
        "          print(\"Position not found\")\n",
        "        else:\n",
        "          newNode.next = current.next\n",
        "          current.next = newNode\n",
        "\n",
        "\n",
        "        #var = Node(item)\n",
        "        #previous_node.next = var\n",
        "        #var.next = previous_node\n",
        "        #previous_node = var\n",
        "\n",
        "    def insertAtEnd(self, item):\n",
        "      var = Node(item)\n",
        "      if self.head == None:\n",
        "        self.head = var\n",
        "      else:\n",
        "        current = self.head\n",
        "        while current.next != None:\n",
        "          current = current.next\n",
        "        current.next =  var\n",
        "\n",
        "    def deleteItem(self, item):\n",
        "      if self.head == None:\n",
        "        return \"Empty queue\"\n",
        "      else:\n",
        "        if self.head.node == item:\n",
        "          self.head = self.head.next\n",
        "        else:\n",
        "          current = self.head\n",
        "          while current != None and current.next.node != item:\n",
        "            current = current.next\n",
        "          if current == None:\n",
        "            return \"Item not found\"\n",
        "          else:\n",
        "            current.next = current.next.next\n",
        "\n",
        "    def display(self):\n",
        "      current = self.head\n",
        "      if current == None:\n",
        "        print(\"Empty LinkedList\")\n",
        "      else:\n",
        "        while current.next != None:\n",
        "          print(current.node, end='-->')\n",
        "          current = current.next\n",
        "        print(current.node)\n",
        "\n",
        "    def search(self, item):\n",
        "      current = self.head\n",
        "      if self.head.node == item:\n",
        "        return True\n",
        "      else:\n",
        "        while current != None:\n",
        "          if current.node == item:\n",
        "            return True\n",
        "          else:\n",
        "            current = current.next\n",
        "        return False\n",
        "\n",
        "    def get_length(self):\n",
        "        current, count = self.head, 0\n",
        "        if self.head == None:\n",
        "          return 0\n",
        "        else:\n",
        "          while current != None:\n",
        "            count += 1\n",
        "            current = current.next\n",
        "          return count\n",
        "\n",
        "    def access(self, index):\n",
        "      current = self.head\n",
        "      if index == 0:\n",
        "        return current.node\n",
        "      else:\n",
        "        count = 0\n",
        "        while count != index and current != None : # or current != None:\n",
        "          current = current.next\n",
        "          count += 1\n",
        "        if current == None:\n",
        "          print(\"Position not found\")\n",
        "        else:\n",
        "          return current.node\n",
        "\n",
        "    def update(self, index, new_data):\n",
        "      current, count = self.head, 0\n",
        "      if current == None:\n",
        "        return \"Empty queue\"\n",
        "      else:\n",
        "        while count != index and current != None:\n",
        "          current = current.next\n",
        "          count +=1\n",
        "        if current == None:\n",
        "          print(\"Out of range\")\n",
        "        else:\n",
        "          current.node = new_data\n",
        "    ### Concatenate ##\n",
        "    def concat(self, x):\n",
        "      current = x.head\n",
        "      if current == None:\n",
        "        self.display()\n",
        "      else:\n",
        "        while current != None:\n",
        "          self.insertAtEnd(current.node)\n",
        "          current = current.next\n",
        "        #self.insertAtEnd(\"None\")\n",
        "        self.display()\n",
        "\n",
        "    ## Reversev a linked_list:\n",
        "    def reverse(self):\n",
        "      current, reversed_lkdl = self.head, LinkedList()\n",
        "\n",
        "      while current != None:\n",
        "        reversed_lkdl.insertAtBeginning(current.node)\n",
        "        current = current.next\n",
        "      reversed_lkdl.display()\n",
        "\n",
        "\n",
        "    ## Sort a Linkedlist in ascending :\n",
        "    def sort(self):\n",
        "      current = self.head\n",
        "      if current == None:\n",
        "        return \"Empty list\"\n",
        "      else:\n",
        "        while current!= None: # and current.next != None:\n",
        "          item1 = current.node\n",
        "          item2 = current.next\n",
        "          if current.next.node <= current.node:\n",
        "            current = current.next\n",
        "            current.next = item2\n",
        "          else:\n",
        "            current = current\n",
        "            current.next = current.next\n",
        "          current = current.next\n",
        "        self.display()\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "linked_list = LinkedList()\n",
        "\n",
        "#display(linked_list)\n",
        "linked_list.insertAtBeginning(2)\n",
        "linked_list.insertAtBeginning(3)\n",
        "linked_list.insertAtBeginning(1)\n",
        "linked_list.insertAtBeginning(1)\n",
        "linked_list.insertAtBeginning(7)\n",
        "linked_list.display()\n",
        "\n",
        "linked_list2 = LinkedList()\n",
        "\n",
        "#display(linked_list)\n",
        "linked_list2.insertAtBeginning(0)\n",
        "linked_list2.insertAtBeginning(6)\n",
        "linked_list2.insertAtBeginning(10)\n",
        "linked_list2.display()\n",
        "\n",
        "linked_list.concat(linked_list2)"
      ],
      "metadata": {
        "id": "ul_Hl0LkRlM4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5c8d3104-8c4c-451f-8133-e757169ef417"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7-->1-->1-->3-->2\n",
            "10-->6-->0\n",
            "7-->1-->1-->3-->2-->10-->6-->0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print( \"Sorted\")\n",
        "linked_list.sort()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 292
        },
        "id": "Y4rHIBh_w6uF",
        "outputId": "ec3e1846-5e77-4d2d-863f-bab65741f81d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sorted\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-236-6f0b8fb553cb>\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m \u001b[0;34m\"Sorted\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mlinked_list\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msort\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-235-f781bdf933e2>\u001b[0m in \u001b[0;36msort\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    154\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0;34m\"Empty list\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    155\u001b[0m       \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 156\u001b[0;31m         \u001b[0;32mwhile\u001b[0m \u001b[0mcurrent\u001b[0m\u001b[0;34m!=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;31m# and current.next != None:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    157\u001b[0m           \u001b[0mitem1\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcurrent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnode\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    158\u001b[0m           \u001b[0mitem2\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcurrent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnext\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "linked_list3 = LinkedList()\n",
        "linked_list2 = LinkedList()\n",
        "\n",
        "#display(linked_list)\n",
        "linked_list2.insertAtBeginning(0)\n",
        "linked_list2.insertAtBeginning(6)\n",
        "linked_list2.insertAtBeginning(10)\n",
        "linked_list2.insertAtEnd(3)\n",
        "linked_list2.display()\n",
        "\n",
        "current = linked_list2.head\n",
        "\n",
        "while current != None:\n",
        "  linked_list3.insertAtBeginning(current.node)\n",
        "  current = current.next\n",
        "\n",
        "linked_list3.display()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "huUBjjsY0p_b",
        "outputId": "278499e7-31e2-4db3-efe1-0befd02ae69c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10-->6-->0-->3\n",
            "3-->0-->6-->10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "Write the function reverse to reverse a linked list\n",
        "\n",
        "Example:\n",
        "\n",
        "Input\n",
        "\n",
        "`my_list = 5 -> 2 -> 7 -> 10 -> 4 -> 6 -> 7 -> `\n",
        "\n",
        "output\n",
        "\n",
        "`reverse_list = 7 -> 6 -> 4 -> 10 -> 7 -> 2 -> 5 -> `"
      ],
      "metadata": {
        "id": "bg2xMdTb7DHN"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "1JAi6FJZ7CdD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Write a function to sort in ascending order elements on the linked list by removing all the duplicated elements.\n",
        "\n",
        "Example:\n",
        "\n",
        "Input\n",
        "\n",
        "`my_list = 5 -> 2 -> 7 -> 10 -> 4 -> 6 -> 7 -> `\n",
        "\n",
        "output\n",
        "\n",
        "`sorted_list = 2 -> 4 -> 5 -> 6 -> 7 -> 10 ->  `"
      ],
      "metadata": {
        "id": "xoNAqkNg7j6c"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Cqrc6g8KRksK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Implement stack using Linked List"
      ],
      "metadata": {
        "id": "6GxcXU3985LM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#class Node:\n",
        "#  def __init__(self):\n",
        "#    self.data = None\n",
        "#    self.next = None\n",
        "\n",
        "class Stack: #(LinkedList):\n",
        "\n",
        "  def __init__(self):\n",
        "   self.stack = LinkedList()\n",
        "   self.length = None\n",
        "   self.last = None\n",
        "\n",
        "  def push(self, item):\n",
        "   self.stack.insertAtEnd(item)\n",
        "\n",
        "  def pop(self):\n",
        "    if self.stack.head == None:\n",
        "      print(\"Empty stack\")\n",
        "    else:\n",
        "      # Stack is not empty:\n",
        "      # get the stack length via LinkedList length\n",
        "      self.length= self.stack.get_length()\n",
        "      ### Access the last element:\n",
        "      self.last = self.stack.access(self.length -1)\n",
        "\n",
        "      ## Delete the last element:\n",
        "      self.stack.deleteItem(self.last)\n",
        "\n",
        "  def display(self):\n",
        "    self.stack.display()\n"
      ],
      "metadata": {
        "id": "JgQiFMcy9Na7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "my_stack = Stack()\n",
        "my_stack.push(1)\n",
        "my_stack.push(2)\n",
        "my_stack.push(3)\n",
        "my_stack.push(4)\n",
        "my_stack.push(5)\n",
        "my_stack.push(6)\n",
        "my_stack.push(7)\n",
        "my_stack.display()\n",
        "#n = my_stack.stack.access(6)\n",
        "#my_stack.stack.deleteItem(n)\n",
        "my_stack.pop()\n",
        "my_stack.pop()\n",
        "\n",
        "my_stack.display()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nnA8LuNFGYtn",
        "outputId": "bab39ef9-4cbd-42e7-b90a-02d27665e842"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1-->2-->3-->4-->5-->6-->7\n",
            "1-->2-->3-->4-->5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "my_stack = Stack()\n",
        "\n",
        "my_stack.push(1)\n",
        "my_stack.push(2)\n",
        "my_stack.push(3)\n",
        "my_stack.push(4)\n",
        "my_stack.push(5)\n",
        "my_stack.push(6)\n",
        "my_stack.push(7)\n",
        "\n",
        "my_stack.pop()\n",
        "my_stack.pop()\n",
        "\n",
        "my_stack.display()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Lyb6N7489X-8",
        "outputId": "123d9022-92c5-41b5-e751-92964d00f508"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the pop element is 7\n",
            "the pop element is 6\n",
            "1 -> 2 -> 3 -> 4 -> 5 -> "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Doubly Linked List\n",
        "\n"
      ],
      "metadata": {
        "id": "xRzOurR2PaAW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "A doubly linked list is a type of linked list in which each node consists of 3 components:\n",
        "\n",
        "* prev - pointer to the previous node\n",
        "* data - data item\n",
        "* next - pointer to the next node\n",
        "\n",
        "![](https://www.programiz.com/sites/tutorial2program/files/doubly-linked-list-created.png)"
      ],
      "metadata": {
        "id": "05O3K7DRPgO-"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Basic Operations\n",
        "\n",
        "\n",
        "\n",
        "*   InsertAtBegining\n",
        "*   InsertAfter\n",
        "*   InsertAtEnd\n",
        "*   Search\n",
        "*   Display\n",
        "*   and all the other basis functions as in Linked List\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "Nbkc37T5RwSF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "    def __init__(self, item):\n",
        "        self.data = item\n",
        "        self.next = None\n",
        "        self.previous = None\n",
        "\n",
        "class DoublyLinkedList:\n",
        "    def __init__(self):\n",
        "      self.head = None\n",
        "\n",
        "\n",
        "    def insert_at_beginning(self, item):\n",
        "        newNode = Node(item)\n",
        "        if self.head !=None:\n",
        "          newNode.next = self.head\n",
        "          self.head.previous = newNode\n",
        "          self.head = newNode\n",
        "        else:\n",
        "          self.head = newNode\n",
        "\n",
        "    def insert_after_index(self, index,item):#previous_node, item):\n",
        "        newNode = Node(item)\n",
        "        current = self.head\n",
        "        if index == 0:\n",
        "          self.insert_at_beginning(item)\n",
        "        else:\n",
        "          count = 0\n",
        "          while count != index and current != None : # or current != None:\n",
        "            current = current.next\n",
        "            count += 1\n",
        "          if current == None:\n",
        "            print(\"Position not found\")\n",
        "          else:\n",
        "            newNode.next = current.next\n",
        "            if current.next != None:\n",
        "              current.next.previous = newNode\n",
        "            current.next = newNode\n",
        "            newNode.previous = current\n",
        "\n",
        "    def insert_at_end(self, item):\n",
        "        newNode  = Node(item)\n",
        "        current = self.head\n",
        "        while current.next !=None:\n",
        "          current = current.next\n",
        "        newNode.previous = current\n",
        "        current.next = newNode\n",
        "\n",
        "\n",
        "\n",
        "    def delete_item(self, item):\n",
        "      # if self.head == None:\n",
        "      #   return \"Empty queue\"\n",
        "      # else:\n",
        "      #   if self.head.node == item:\n",
        "      #     self.head = self.head.next\n",
        "      #   else:\n",
        "      #     current = self.head\n",
        "      #     while current != None and current.next.node != item:\n",
        "      #           current = current.next\n",
        "      #     if current == None:\n",
        "      #           return \"Item not found\"\n",
        "      #     else:\n",
        "      #        current.next = current.next.next\n",
        "\n",
        "      if self.head == None:\n",
        "        return \"Empty queue\"\n",
        "      else:\n",
        "        if self.head.data == item:\n",
        "          self.head = self.head.next\n",
        "          self.head.next.previous = None\n",
        "        else:\n",
        "          current = self.head\n",
        "          while current != None and current.next.data != item:\n",
        "            current = current.next\n",
        "          if current == None:\n",
        "            return \"Item not found\"\n",
        "          else:\n",
        "            current.next = current.next.next\n",
        "            current.next.previous = current\n",
        "\n",
        "    def search(self, item):\n",
        "      current = self.head\n",
        "      if self.head.data == item:\n",
        "        return True\n",
        "      else:\n",
        "        while current != None:\n",
        "          if current.data == item:\n",
        "            return True\n",
        "          else:\n",
        "            current = current.next\n",
        "        return False\n",
        "\n",
        "    def get_length(self):\n",
        "        current, count = self.head, 0\n",
        "        if self.head == None:\n",
        "          return 0\n",
        "        else:\n",
        "          while current != None:\n",
        "            count += 1\n",
        "            current = current.next\n",
        "          return count\n",
        "\n",
        "    def access(self, index):\n",
        "      current, = self.head\n",
        "      if index == 0:\n",
        "        return current.data\n",
        "      else:\n",
        "        count = 0\n",
        "        while count != index and current != None : # or current != None:\n",
        "          current = current.next\n",
        "          count += 1\n",
        "        if current == None:\n",
        "          print(\"Position not found\")\n",
        "        else:\n",
        "          return current.data\n",
        "\n",
        "    def update(self, index, new_data):\n",
        "      current, count = self.head, 0\n",
        "      if current == None:\n",
        "        return \"Empty queue\"\n",
        "      else:\n",
        "        while count != index and current != None:\n",
        "          current = current.next\n",
        "          count +=1\n",
        "        if current == None:\n",
        "          print(\"Out of range\")\n",
        "        else:\n",
        "          current.data = new_data\n",
        "\n",
        "    def display(self):\n",
        "      current = self.head\n",
        "      if current == None:\n",
        "        print(\"Empty LinkedList\")\n",
        "      else:\n",
        "        while current.next != None:\n",
        "          print(current.data, end='<-->')\n",
        "          current = current.next\n",
        "        print(current.data)"
      ],
      "metadata": {
        "id": "Jq7lAQeJPdLm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "d_linked_list = DoublyLinkedList()\n",
        "\n",
        "d_linked_list.insert_at_beginning(1)\n",
        "d_linked_list.insert_at_beginning(3)\n",
        "d_linked_list.insert_at_beginning(0)\n",
        "d_linked_list.display()\n",
        "\n",
        "d_linked_list.insert_at_end(5)\n",
        "d_linked_list.insert_at_end(90)\n",
        "d_linked_list.display()\n",
        "\n",
        "d_linked_list.insert_after_index(2,7)\n",
        "d_linked_list.display()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hfKF7jaw5zjO",
        "outputId": "39b7096c-b162-4559-d3e2-d1d598f7f809"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0<-->3<-->1\n",
            "0<-->3<-->1<-->5<-->90\n",
            "0<-->3<-->1<-->7<-->5<-->90\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "d_linked_list.delete_item(1)\n",
        "d_linked_list.display()"
      ],
      "metadata": {
        "id": "WxT46KJ_DH_J",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fa6d8c21-ea2f-4567-f64a-d4ffb29e75d9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0<-->3<-->7<-->5<-->90\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "d_linked_list = DoublyLinkedList()\n",
        "\n",
        "d_linked_list.insert_at_end(5)\n",
        "d_linked_list.display()\n",
        "d_linked_list.insert_at_beginning(1)\n",
        "d_linked_list.display()\n",
        "\n",
        "d_linked_list.insert_at_beginning(6)\n",
        "d_linked_list.display()\n",
        "\n",
        "d_linked_list.insert_at_end(9)\n",
        "d_linked_list.display()\n",
        "\n",
        "\n",
        "print(f\"6 is inside the list : \", d_linked_list.search(6))\n",
        "\n",
        "# insert 11 after head\n",
        "d_linked_list.insert_after(d_linked_list.head, 11)\n",
        "\n",
        "# insert 15 after the seond node\n",
        "d_linked_list.insert_after(d_linked_list.head.next, 15)\n",
        "\n",
        "\n",
        "d_linked_list.display()\n",
        "\n",
        "d_linked_list.delete_item(1)\n",
        "d_linked_list.display()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 326
        },
        "id": "5KWrGOKqPmEB",
        "outputId": "50d1d9e6-9eef-43f3-a688-bd90cde49023"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "AttributeError",
          "evalue": "'NoneType' object has no attribute 'next'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-5-5b2b37556068>\u001b[0m in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0md_linked_list\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mDoublyLinkedList\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0md_linked_list\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minsert_at_end\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0md_linked_list\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdisplay\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0md_linked_list\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minsert_at_beginning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-2-45da57c7c19e>\u001b[0m in \u001b[0;36minsert_at_end\u001b[0;34m(self, item)\u001b[0m\n\u001b[1;32m     41\u001b[0m         \u001b[0mnewNode\u001b[0m  \u001b[0;34m=\u001b[0m \u001b[0mNode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mitem\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     42\u001b[0m         \u001b[0mcurrent\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhead\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 43\u001b[0;31m         \u001b[0;32mwhile\u001b[0m \u001b[0mcurrent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnext\u001b[0m \u001b[0;34m!=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     44\u001b[0m           \u001b[0mcurrent\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcurrent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnext\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     45\u001b[0m         \u001b[0mnewNode\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprevious\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcurrent\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'next'"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Exercises"
      ],
      "metadata": {
        "id": "CQSaT6QkR0jU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "Write the function reverse to reverse a linked list\n",
        "\n",
        "Example:\n",
        "\n",
        "Input\n",
        "\n",
        "`my_list = 5 <-> 2 <-> 7 <-> 10 <-> 4 <-> 6 <-> 7 <-> `\n",
        "\n",
        "output\n",
        "\n",
        "`reverse_list = 7 <-> 6 <-> 4 <-> 10 <-> 7 <-> 2 <-> 5 <-> `"
      ],
      "metadata": {
        "id": "Fr71fjYcEG3n"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "0at8xRcoEG30"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "Implement Queue usind DoubleLinkedList"
      ],
      "metadata": {
        "id": "ZaB4BpYQERK8"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "eXIzjpiqR3dp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Binary Tree"
      ],
      "metadata": {
        "id": "bUCvbKXED0Nr"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Tree is a non linear hierarchical data structure where nodes are connected by edges. The binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.\n",
        "\n",
        "![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/1200px-Binary_search_tree.svg.png)\n",
        "\n",
        "image credit: https://en.wikipedia.org/wiki/Binary_search_tree\n",
        "\n",
        "The topmost node is called root and the  bottommost nodes or the nodes with no children are called the leaf nodes. A node contains:\n",
        "\n",
        "* Data\n",
        "* Pointer to left child\n",
        "* Pointer to the right child\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "wxZQZTm-P8RL"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "#### Basic Operations\n",
        "\n",
        "\n",
        "*   Inserting an element\n",
        "*   Searching for an element.\n",
        "*   Deletion for an element.\n",
        "*   Traversing an element.\n",
        "\n",
        "\n",
        "\n",
        "There are three ways to visite/traverse each node present in the tree exactly once\n",
        "\n",
        "\n",
        "*   Inorder: left subtree, root, right subtree\n",
        "*   Preorder: root, left subtree, right subtree\n",
        "*   Postorder: left subtree, right subtree, root"
      ],
      "metadata": {
        "id": "Lv-sd1jWTtXB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "  def __init__(self, data):\n",
        "    self.data = data\n",
        "    self.left =None\n",
        "    self.right =None\n",
        "\n",
        "\n",
        "\n",
        "class BinaryTree:\n",
        "\n",
        "  def __init__(self):\n",
        "    self.root = None\n",
        "\n",
        "  def addNode(self, data):\n",
        "    newNode = Node(data)\n",
        "    if self.root == None:\n",
        "      self.root = newNode\n",
        "      self.root.data = data\n",
        "    else:\n",
        "      current = self.root\n",
        "      while current != None:\n",
        "        if newNode.data < current.data:\n",
        "          flag = current\n",
        "          current = current.left\n",
        "        else:\n",
        "          flag = current\n",
        "          current = current.right\n",
        "      if flag.data < newNode.data:\n",
        "        flag.right = newNode\n",
        "      elif flag.data > newNode.data:\n",
        "        flag.left = newNode\n",
        "      else:\n",
        "        pass\n",
        "\n",
        "\n",
        "  def is_leave(self,data):\n",
        "    node = Node(data)\n",
        "    if node.left == None and node == None:\n",
        "      return True\n",
        "    else:\n",
        "      return False\n",
        "\n",
        "  def searchNode(self, data):\n",
        "    if self.root == None:\n",
        "      return \"Empty tree\"\n",
        "    if self.root.data == data:\n",
        "      print(True)\n",
        "    else:\n",
        "      if self.root.right !=None and self.root.data < data:\n",
        "        self.root = self.root.right\n",
        "        self.searchNode(self.root.data)\n",
        "      if data <= self.root.data and self.root.left !=None:\n",
        "        self.root = self.root.left\n",
        "        self.searchNode(self.root.data)\n",
        "      else:\n",
        "        print(\"Item not found\")\n",
        "\n",
        "\n",
        "\n",
        "  def deleteNode(self, data):\n",
        "    current = self.root\n",
        "    temp = self.root\n",
        "\n",
        "    while current !=None and current.data !=data:\n",
        "      if current.data <data:\n",
        "        temp = current\n",
        "        current = current.right\n",
        "      else:\n",
        "        temp = current\n",
        "        current = current.left\n",
        "    if current == None:\n",
        "      print(f\"{data} not found\")\n",
        "    elif temp.data > current.data and temp.left.left ==None and temp.left.right == None:\n",
        "      temp.left = None\n",
        "    elif temp.data <current.data and temp.right.left == None and temp.right.right == None:\n",
        "     temp.right == None\n",
        "    else:\n",
        "      flag = current.right\n",
        "      while flag.left != None:\n",
        "        flag_previous = flag\n",
        "        flag = flag.left\n",
        "\n",
        "      flag.left = current.left\n",
        "      flag.right = current.right\n",
        "      if temp.data < current.data:\n",
        "        temp.right = flag\n",
        "        flag_previous.left = None\n",
        "      else:\n",
        "        temp.left = flag\n",
        "        flag_previous.left = None\n",
        "\n",
        "\n",
        "  def printInorder(self, root):\n",
        "    if root == None:\n",
        "      return\n",
        "    else:\n",
        "\n",
        "      self.printInorder(root.left)\n",
        "      print(root.data, end =\"-->\")\n",
        "      self.printInorder(root.right)\n",
        "      return\n",
        "\n",
        "  def printPreOrder(self, root):\n",
        "    if root == None:\n",
        "      return\n",
        "    else:\n",
        "      self.printPreOrder(root.left)\n",
        "      self.printPreOrder(root.right)\n",
        "      print(root.data, end = \"-->\")\n",
        "    # print(printInorder(self.root))\n",
        "    # print(printInorder(self.root.left))\n",
        "    # print(printInorder(self.root.right))\n",
        "\n",
        "  def printPostOrder(self, root):\n",
        "    if root == None:\n",
        "      return\n",
        "    else:\n",
        "\n",
        "      self.printPreOrder(root.left)\n",
        "      self.printPreOrder(root.right)\n",
        "      print(root.data, end = \"-->\")\n",
        "    # print(printPostOrder(self.root.left))\n",
        "    # print(printPostOrder(self.root.right))\n",
        "    # print(printPostOrder(self.root))\n",
        "\n"
      ],
      "metadata": {
        "id": "N0771w0tI07y"
      },
      "execution_count": 289,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "bnTree = BinaryTree()\n",
        "bnTree.addNode(8)\n",
        "bnTree.addNode(3)\n",
        "bnTree.addNode(6)\n",
        "bnTree.addNode(4)\n",
        "bnTree.addNode(7)\n",
        "bnTree.addNode(14)\n",
        "bnTree.addNode(13)\n",
        "bnTree.addNode(1)\n",
        "bnTree.addNode(10)\n",
        "#bnTree.addNode(17)\n",
        "#bnTree.addNode(16)\n",
        "#bnTree.addNode(37)\n",
        "# bnTree.addNode(0)\n",
        "# bnTree.addNode(3)\n",
        "# bnTree.addNode(19)\n",
        "# bnTree.printInorder(bnTree)\n",
        "#bnTree.searchNode(6)\n",
        "bnTree.printInorder(bnTree.root)\n",
        "print(\" \", end =\"\\n\")\n",
        "bnTree.printPreOrder(bnTree.root)\n",
        "\n",
        "#print(bnTree.root.left.left.right.data)\n",
        "\n"
      ],
      "metadata": {
        "id": "aZWiZKj16uog",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "605c5383-1850-45e8-d3d3-b6985f97c370"
      },
      "execution_count": 291,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1-->3-->4-->6-->7-->8-->10-->13-->14--> \n",
            "1-->4-->7-->6-->3-->10-->13-->14-->8-->"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "bnTree.printInorder(bnTree.root)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AGeFFYERBOM-",
        "outputId": "12b20dbc-501a-41c8-b82d-9bdc83d19549"
      },
      "execution_count": 255,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3-->4-->6-->7-->8-->10-->13-->14-->"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"========\")\n",
        "bnTree.deleteNode(3)\n",
        "bnTree.printInorder(bnTree.root)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jgFzqMb9e97R",
        "outputId": "d77c512b-3884-48d0-da7a-ad23bf3785f6"
      },
      "execution_count": 259,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "========\n",
            "4-->6-->7-->8-->13-->14-->"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Exercises"
      ],
      "metadata": {
        "id": "wUmwDdLrJErr"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Based on the previous class, write the function Inorder."
      ],
      "metadata": {
        "id": "j4V4pHWiJMAQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def printInorder(b_tree):\n",
        "  pass"
      ],
      "metadata": {
        "id": "LUGy5SxpIM6m"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Based on the previous class, write the function Preorder."
      ],
      "metadata": {
        "id": "6ounE44_JgQ1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def printPreOrder(b_tree):\n",
        "  pass"
      ],
      "metadata": {
        "id": "soY475x_JiQw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### Exercise\n",
        "\n",
        "Based on the previous class, write the function Postorder."
      ],
      "metadata": {
        "id": "vDrfoTS6Jnzc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def printPostOrder(b_tree):\n",
        "  pass"
      ],
      "metadata": {
        "id": "m2K3srAGJpli"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "D3lLzHN1-1IF"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}