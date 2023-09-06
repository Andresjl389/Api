import os
import mysql.connector #pip install mysql-connector-python
from datetime import date
from functools import wraps
from flask import Flask, jsonify, request