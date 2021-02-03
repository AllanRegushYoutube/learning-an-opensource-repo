#!/usr/bin/python

def a(j):
  """
  Add two values
  """
  return j


def main():
  """
  Main Function
  """
  v = input("Enter a number: ")
  assert type(v) is int
  print(a(v))




main()
