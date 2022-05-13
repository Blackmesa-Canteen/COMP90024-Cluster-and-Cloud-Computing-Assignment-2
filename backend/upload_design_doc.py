# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     upload_design_doc
   Description :  upload design docs for map-reduce functions
   Author :       Bocan Yang
   date:          5/05/2022
-------------------------------------------------
"""
import json
import requests
from util import config_handler as cfg_handler

aurin_employment_doc = {
  "_id": "_design/scenario",
  "views": {
    "employment_sum": {
      "reduce": "_sum",
      "map": "function (doc) {\n  if (doc.num_2019_3 && doc.num_2019_3 != \"null\") {\n    emit(\"employment-2019-s1\", parseInt(doc.num_2019_3))\n  }\n  if (doc.num_2019_6 && doc.num_2019_6 != \"null\") {\n    emit(\"employment-2019-s2\", parseInt(doc.num_2019_6))\n  }\n  if (doc.num_2019_9 && doc.num_2019_9 != \"null\") {\n    emit(\"employment-2019-s3\", parseInt(doc.num_2019_9))\n  }\n  if (doc.num_2019_12 && doc.num_2019_12 != \"null\") {\n    emit(\"employment-2019-s4\", parseInt(doc.num_2019_12))\n  }\n  if (doc.num_2020_3 && doc.num_2020_3 != \"null\") {\n    emit(\"employment-2020-s1\", parseInt(doc.num_2020_3))\n  }\n  if (doc.num_2020_6 && doc.num_2020_6 != \"null\") {\n    emit(\"employment-2020-s2\", parseInt(doc.num_2020_6))\n  }\n  if (doc.num_2020_9 && doc.num_2020_9 != \"null\") {\n    emit(\"employment-2020-s3\", parseInt(doc.num_2020_9))\n  }\n  if (doc.num_2020_12 && doc.num_2020_12 != \"null\") {\n    emit(\"employment-2020-s4\", parseInt(doc.num_2020_12))\n  }\n  if (doc.num_2021_3 && doc.num_2021_3 != \"null\") {\n    emit(\"employment-2021-s1\", parseInt(doc.num_2021_3))\n  }\n  if (doc.num_2021_6 && doc.num_2021_6 != \"null\") {\n    emit(\"employment-2021-s2\", parseInt(doc.num_2021_6))\n  }\n  if (doc.num_2021_9 && doc.num_2021_9 != \"null\") {\n    emit(\"employment-2021-s3\", parseInt(doc.num_2021_9))\n  }\n}"
    },
    "unemployment_sum": {
      "reduce": "_sum",
      "map": "function (doc) {\n  if (doc.un_num_2019_3 && doc.un_num_2019_3 != \"null\") {\n    emit(\"unemployment-2019-s1\", parseInt(doc.un_num_2019_3))\n  }\n  if (doc.un_num_2019_6 && doc.un_num_2019_6 != \"null\") {\n    emit(\"unemployment-2019-s2\", parseInt(doc.un_num_2019_6))\n  }\n  if (doc.un_num_2019_9 && doc.un_num_2019_9 != \"null\") {\n    emit(\"unemployment-2019-s3\", parseInt(doc.un_num_2019_9))\n  }\n  if (doc.un_num_2019_12 && doc.un_num_2019_12 != \"null\") {\n    emit(\"unemployment-2019-s4\", parseInt(doc.un_num_2019_12))\n  }\n  if (doc.un_num_2020_3 && doc.un_num_2020_3 != \"null\") {\n    emit(\"unemployment-2020-s1\", parseInt(doc.un_num_2020_3))\n  }\n  if (doc.un_num_2020_6 && doc.un_num_2020_6 != \"null\") {\n    emit(\"unemployment-2020-s2\", parseInt(doc.un_num_2020_6))\n  }\n  if (doc.un_num_2020_9 && doc.un_num_2020_9 != \"null\") {\n    emit(\"unemployment-2020-s3\", parseInt(doc.un_num_2020_9))\n  }\n  if (doc.un_num_2020_12 && doc.un_num_2020_12 != \"null\") {\n    emit(\"unemployment-2020-s4\", parseInt(doc.un_num_2020_12))\n  }\n  if (doc.un_num_2021_3 && doc.un_num_2021_3 != \"null\") {\n    emit(\"unemployment-2021-s1\", parseInt(doc.un_num_2021_3))\n  }\n  if (doc.un_num_2021_6 && doc.un_num_2021_6 != \"null\") {\n    emit(\"unemployment-2021-s2\", parseInt(doc.un_num_2021_6))\n  }\n  if (doc.un_num_2021_9 && doc.un_num_2021_9 != \"null\") {\n    emit(\"unemployment-2021-s3\", parseInt(doc.un_num_2021_9))\n  }\n}"
    },
    "unemployment_rate_sum": {
      "reduce": "function (keys, values, rereduce) {\n    return sum(values) / values.length;\n}",
      "map": "function (doc) {\n  if (doc.un_rate_2019_3 && doc.un_rate_2019_3 != \"null\") {\n    emit(\"unemployment-rate-2019-s1\", parseFloat(doc.un_rate_2019_3))\n  }\n  if (doc.un_rate_2019_6 && doc.un_rate_2019_6 != \"null\") {\n    emit(\"unemployment-rate-2019-s2\", parseFloat(doc.un_rate_2019_6))\n  }\n  if (doc.un_rate_2019_9 && doc.un_rate_2019_9 != \"null\") {\n    emit(\"unemployment-rate-2019-s3\", parseFloat(doc.un_rate_2019_9))\n  }\n  if (doc.un_rate_2019_12 && doc.un_rate_2019_12 != \"null\") {\n    emit(\"unemployment-rate-2019-s4\", parseFloat(doc.un_rate_2019_12))\n  }\n  if (doc.un_rate_2020_3 && doc.un_rate_2020_3 != \"null\") {\n    emit(\"unemployment-rate-2020-s1\", parseFloat(doc.un_rate_2020_3))\n  }\n  if (doc.un_rate_2020_6 && doc.un_rate_2020_6 != \"null\") {\n    emit(\"unemployment-rate-2020-s2\", parseFloat(doc.un_rate_2020_6))\n  }\n  if (doc.un_rate_2020_9 && doc.un_rate_2020_9 != \"null\") {\n    emit(\"unemployment-rate-2020-s3\", parseFloat(doc.un_rate_2020_9))\n  }\n  if (doc.un_rate_2020_12 && doc.un_rate_2020_12 != \"null\") {\n    emit(\"unemployment-rate-2020-s4\", parseFloat(doc.un_rate_2020_12))\n  }\n  if (doc.un_rate_2021_3 && doc.un_rate_2021_3 != \"null\") {\n    emit(\"unemployment-rate-2021-s1\", parseFloat(doc.un_rate_2021_3))\n  }\n  if (doc.un_rate_2021_6 && doc.un_rate_2021_6 != \"null\") {\n    emit(\"unemployment-rate-2021-s2\", parseFloat(doc.un_rate_2021_6))\n  }\n  if (doc.un_rate_2021_9 && doc.un_rate_2021_9 != \"null\") {\n    emit(\"unemployment-rate-2021-s3\", parseFloat(doc.un_rate_2021_9))\n  }\n}"
    }
  },
  "language": "javascript"
}

aurin_house_price_doc = {
  "_id": "_design/scenario",
  "views": {
    "sale_quarter_pos_type": {
      "map": "function (doc) {\n  if (doc.year && doc.month) {\n    var monthInt = parseInt(doc.month);\n    var quarter = \"unkown\"\n    if (monthInt <= 3) {\n      quarter = \"s1\"\n    } else if (monthInt <= 6) {\n      quarter = \"s2\"\n    } else if (monthInt <= 9) {\n      quarter = \"s3\"\n    } else {\n      quarter = \"s4\"\n    }\n  }\n  if (doc.sale_avg && doc.sale_max) {\n    emit([doc.year, quarter, doc.position, doc.type], [parseFloat(doc.sale_avg), parseFloat(doc.sale_max)])\n  }\n}"
    }
  },
  "language": "javascript"
}

aurin_income_doc = {
  "_id": "_design/scenario",
  "views": {
    "income_year_pos": {
      "reduce": "_sum",
      "map": "function (doc) {\n  if(doc.year!=\"null\" && doc.mean_employee_income_year != \"null\" && doc.position != \"null\")\n  emit([doc.year,doc.position],parseFloat(doc.mean_employee_income_year));\n}"
    },
    "income_pos": {
      "reduce": "_stats",
      "map": "function (doc) {\n  if(doc.position!=\"null\"&&doc.mean_employee_income_year!=\"null\")\n  emit(doc.position,parseFloat(doc.mean_employee_income_year));\n}"
    },
    "income_year": {
      "reduce": "_stats",
      "map": "function (doc) {\n  if(doc.year!=\"null\"&&doc.mean_employee_income_year!=\"null\")\n  emit(doc.year,parseFloat(doc.mean_employee_income_year));\n}"
    }
  },
  "language": "javascript"
}

aurin_migration_doc = {
  "_id": "_design/scenario",
  "views": {
    "population_sum": {
      "reduce": "_sum",
      "map": "function (doc) {\n  if (doc.person_num && doc.year) {\n    emit(doc.year, parseInt(doc.person_num))\n  }\n}"
    },
    "total_population_sum": {
      "reduce": "_sum",
      "map": "function (doc) {\n  if (doc.birth_2016_num && doc.population_2016) {\n      emit('2016-birth', parseInt(doc.birth_2016_num))\n      emit('2016', parseInt(doc.population_2016))\n  }\n  if (doc.birth_2017_num && doc.population_2017) {\n      emit('2017-birth', parseInt(doc.birth_2017_num))\n      emit('2017', parseInt(doc.population_2017))\n  }\n  if (doc.birth_2018_num && doc.population_2018) {\n      emit('2018-birth', parseInt(doc.birth_2018_num))\n      emit('2018', parseInt(doc.population_2018))\n  }\n  if (doc.birth_2019_num && doc.population_2019) {\n      emit('2019-birth', parseInt(doc.birth_2019_num))\n      emit('2019', parseInt(doc.population_2019))\n  }\n  if (doc.birth_2020_num && doc.population_2020) {\n      emit('2020-birth', parseInt(doc.birth_2020_num) )\n      emit('2020', parseInt(doc.population_2020))\n  }\n}"
    },
    "year_sum": {
      "reduce": "_sum",
      "map": "function (doc) {\n  if (doc.year && doc.age_all) {\n    emit(doc.year, parseFloat(doc.age_all)); \n  }\n}"
    }
  },
  "language": "javascript"
}

languages_doc = {
  "_id": "_design/languages",
  "views": {
    "language_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.lang) {\n    emit(doc.lang, 1);\n  }\n}"
    },
    "language_month_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.lang && doc.created_at) {\n    var strDate = doc.created_at.toString();\n    var year = strDate.slice(0, 4)\n    var month = strDate.slice(5, 7)\n    emit([year, month, doc.lang], 1);\n  }\n}"
    },
    "language_quarter_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.lang && doc.created_at) {\n    var strDate = doc.created_at.toString();\n    var year = strDate.slice(0, 4)\n    var month = strDate.slice(5, 7)\n    var monthInt = parseInt(month)\n    var quarter = \"unknown\"\n    if (monthInt <= 3) {\n      quarter = \"s1\"\n    } else if (monthInt <= 6) {\n      quarter = \"s2\"\n    } else if (monthInt <= 9) {\n      quarter = \"s3\"\n    } else {\n      quarter = \"s4\"\n    }\n    emit([year, quarter, doc.lang], 1);\n  }\n}"
    },
    "language_year_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.lang && doc.created_at) {\n    var strDate = doc.created_at.toString();\n    var year = strDate.slice(0, 4)\n    emit([year, doc.lang], 1);\n  }\n}"
    }
  },
  "language": "javascript"
}

covid_locadown_doc = {
  "_id": "_design/scenario",
  "views": {
    "polarity_day_avg": {
      "reduce": "function (keys, values, rereduce) {\n    return sum(values) / values.length;\n}",
      "map": "function (doc) {\n  if (doc.polarity && doc.created_at) {\n    var strDate = doc.created_at.toString();\n    var year = strDate.slice(0, 4)\n    var month = strDate.slice(5, 7)\n    var day = strDate.slice(8, 10)\n    emit([year, month, day], parseFloat(doc.polarity));\n  }\n}"
    }
  },
  "language": "javascript"
}

covid_doc = {
  "_id": "_design/scenario",
  "views": {
    "polarity_day_avg": {
      "reduce": "function (keys, values, rereduce) {\n    return sum(values) / values.length;\n}",
      "map": "function (doc) {\n  if (doc.polarity && doc.created_at) {\n    var strDate = doc.created_at.toString();\n    var year = strDate.slice(0, 4)\n    var month = strDate.slice(5, 7)\n    var day = strDate.slice(8, 10)\n    emit([year, month, day], parseFloat(doc.polarity));\n  }\n}"
    },
    "map_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.coordinates) {\n    long = doc.coordinates.coordinates[0]\n    lati = doc.coordinates.coordinates[1]\n    if (long == 144.9631 && lati == 37.8136) {\n      random = Math.floor(Math.random()*100000)\n      if (random <= 43114) {\n        emit(\"Melbourne - Inner\", 1);\n        emit(\"206\", 1);\n      } else if (random <= 54181) {\n        emit(\"Melbourne - North East\", 1);\n        emit(\"209\", 1);\n      } else if (random <= 62454) {\n        emit(\"Melbourne - Outer East\", 1);\n        emit(\"211\", 1);\n      } else if (random <= 70722) {\n        emit(\"Melbourne - Inner South\", 1);\n        emit(\"208\", 1);\n      } else if (random <= 78526) {\n        emit(\"Melbourne - West\", 1);\n        emit(\"213\", 1);\n      } else if (random <= 85960) {\n        emit(\"Melbourne - South East\", 1);\n        emit(\"212\", 1);\n      } else if (random <= 93255) {\n        emit(\"Melbourne - Inner East\", 1);\n        emit(\"207\", 1);\n      } else if (random <= 99412) {\n        emit(\"Melbourne - North West\", 1);\n        emit(\"210\", 1);\n      } else if (random <= 99771) {\n        emit(\"Other Place\", 1);\n        emit(\"-1\", 1);\n      } else {\n        emit(\"Mornington Peninsula\", 1);\n        emit(\"214\", 1);\n      }\n    }\n  }\n}"
    },
    "map_year_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.created_at) {\n    var strDate = doc.created_at.toString();\n    var year = strDate.slice(0, 4)\n  }\n  if (doc.coordinates) {\n    long = doc.coordinates.coordinates[0]\n    lati = doc.coordinates.coordinates[1]\n    if (long == 144.9631 && lati == 37.8136) {\n      random = Math.floor(Math.random()*100000)\n      if (random <= 43114) {\n        emit([year, \"Melbourne - Inner\"], 1);\n        emit([year, \"206\"], 1);\n      } else if (random <= 54181) {\n        emit([year, \"Melbourne - North East\"], 1);\n        emit([year, \"209\"], 1);\n      } else if (random <= 62454) {\n        emit([year, \"Melbourne - Outer East\"], 1);\n        emit([year, \"211\"], 1);\n      } else if (random <= 70722) {\n        emit([year, \"Melbourne - Inner South\"], 1);\n        emit([year, \"208\"], 1);\n      } else if (random <= 78526) {\n        emit([year, \"Melbourne - West\"], 1);\n        emit([year, \"213\"], 1);\n      } else if (random <= 85960) {\n        emit([year, \"Melbourne - South East\"], 1);\n        emit([year, \"212\"], 1);\n      } else if (random <= 93255) {\n        emit([year, \"Melbourne - Inner East\"], 1);\n        emit([year, \"207\"], 1);\n      } else if (random <= 99412) {\n        emit([year, \"Melbourne - North West\"], 1);\n        emit([year, \"210\"], 1);\n      } else if (random <= 99771) {\n        emit([year, \"Other Place\"], 1);\n        emit([year, \"-1\"], 1);\n      } else {\n        emit([year, \"Mornington Peninsula\"], 1);\n        emit([year, \"214\"], 1);\n      }\n    }\n  }\n}"
    }
  },
  "language": "javascript"
}

house_price_doc = {
  "_id": "_design/scenario",
  "views": {
    "map_polarity_quarter_avg": {
      "reduce": "function (keys, values, rereduce) {\n    return sum(values) / values.length;\n}",
      "map": "function (doc) {\n  if (doc.created_at) {\n    var strDate = doc.created_at.toString();\n    var year = strDate.slice(0, 4)\n    var month = strDate.slice(5, 7)\n    var monthInt = parseInt(month)\n    var quarter = \"unknown\"\n    if (monthInt <= 3) {\n      quarter = \"s1\"\n    } else if (monthInt <= 6) {\n      quarter = \"s2\"\n    } else if (monthInt <= 9) {\n      quarter = \"s3\"\n    } else {\n      quarter = \"s4\"\n    }\n  }\n  var time = year + \"-\" + quarter\n  if (doc.coordinates && doc.polarity) {\n    var pola = doc.polarity\n    var long = doc.coordinates.coordinates[0]\n    var lati = doc.coordinates.coordinates[1]\n    if (lati >= 0) {\n      lati = -lati\n    }\n    if (long >= 144.8890 && long <= 145.0450 && lati >= -37.8910 && lati <= -37.7340) {\n      emit([time, \"Melbourne - Inner\"], parseFloat(pola));\n    } else if (long >= 144.9993 && long <= 145.1841 && lati >= -37.8759 && lati <= -37.7340){\n      emit([time, \"Melbourne - Inner East\"], parseFloat(pola));\n    } else if (long >= 144.9850 && long <= 145.1560 && lati >= -38.0850 && lati <= -37.8370) {\n      emit([time, \"Melbourne - Inner South\"], parseFloat(pola));\n    } else if (long >= 144.8810 && long <= 145.5800 && lati >= -37.7840 && lati <= -37.2630) {\n      emit([time, \"Melbourne - North East\"], parseFloat(pola));\n    } else if (long >= 144.4593 && long <= 144.9853 && lati >= -37.7730 && lati <= -37.1751) {\n      emit([time, \"Melbourne - North West\"], parseFloat(pola));\n    } else if (long >= 145.1569 && long <= 145.8784 && lati >= -37.9747 && lati <= -37.5266) {\n      emit([time, \"Melbourne - Outer East\"], parseFloat(pola));\n    } else if (long >= 145.0800 && long <= 145.7650 && lati >= -38.3320 && lati <= -37.8530) {\n      emit([time, \"Melbourne - South East\"], parseFloat(pola));\n    } else if (long >= 144.3340 && long <= 144.9160 && lati >= -38.0040 && lati <= -37.5460) {\n      emit([time, \"Melbourne - West\"], parseFloat(pola));\n    } else if (long >= 144.6520 && long <= 145.2620 && lati >= -38.5030 && lati <= -38.0670) {\n      emit([time, \"Mornington Peninsula\"], parseFloat(pola));\n    } else {\n      emit([time, \"Other Place\"], parseFloat(pola));\n    }\n  }\n}"
    },
    "polarity_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.polarity>0.5 && doc.polarity<=1) {\n    emit(\"very positive\",1)\n  } else if (doc.polarity<-0.5 && doc.polarity>=-1) {\n    emit(\"very negative\",1)\n  } else if (doc.polarity > 0.1 && doc.polarity<=0.5) {\n    emit(\"positive\",1)\n  } else if (doc.polarity<-0.1 && doc.polarity>=-0.5) {\n    emit(\"negative\",1)\n  } else {\n    emit(\"netural\",1)\n  }\n}"
    },
    "subjectivity_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.subjectivity) {\n    var num = doc.subjectivity;\n    if (num <= 0.2)  {\n        emit(\"very objective\", 1);\n    } else if (num <= 0.4) {\n      emit(\"objective\", 1);\n    } else if (num <= 0.6) {\n      emit(\"normal\", 1);\n    } else if (num <= 0.8) {\n       emit(\"subjective\", 1);\n    } else if (num <= 1.0) {\n      emit(\"very subjective\", 1);\n    } else {\n      emit(\"unkown\", 1);\n    }\n  } \n}"
    },
    "year_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.created_at) {\n    var strDate = doc.created_at.toString();\n    var year = strDate.slice(0, 4)\n    emit(year, 1);\n  }\n}"
    },
    "map_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.coordinates) {\n    long = doc.coordinates.coordinates[0]\n    lati = doc.coordinates.coordinates[1]\n    if (lati >= 0) {\n      lati = -lati\n    }\n    if (long >= 144.8890 && long <= 145.0450 && lati >= -37.8910 && lati <= -37.7340) {\n      emit(\"Melbourne - Inner\", 1);\n      emit(\"206\", 1);\n    } else if (long >= 144.9993 && long <= 145.1841 && lati >= -37.8759 && lati <= -37.7340){\n      emit(\"Melbourne - Inner East\", 1);\n      emit(\"207\", 1);\n    } else if (long >= 144.9850 && long <= 145.1560 && lati >= -38.0850 && lati <= -37.8370) {\n      emit(\"Melbourne - Inner South\", 1);\n      emit(\"208\", 1);\n    } else if (long >= 144.8810 && long <= 145.5800 && lati >= -37.7840 && lati <= -37.2630) {\n      emit(\"Melbourne - North East\", 1);\n      emit(\"209\", 1);\n    } else if (long >= 144.4593 && long <= 144.9853 && lati >= -37.7730 && lati <= -37.1751) {\n      emit(\"Melbourne - North West\", 1);\n      emit(\"210\", 1);\n    } else if (long >= 145.1569 && long <= 145.8784 && lati >= -37.9747 && lati <= -37.5266) {\n      emit(\"Melbourne - Outer East\", 1);\n      emit(\"211\", 1);\n    } else if (long >= 145.0800 && long <= 145.7650 && lati >= -38.3320 && lati <= -37.8530) {\n      emit(\"Melbourne - South East\", 1);\n      emit(\"212\", 1);\n    } else if (long >= 144.3340 && long <= 144.9160 && lati >= -38.0040 && lati <= -37.5460) {\n      emit(\"Melbourne - West\", 1);\n      emit(\"213\", 1);\n    } else if (long >= 144.6520 && long <= 145.2620 && lati >= -38.5030 && lati <= -38.0670) {\n      emit(\"Mornington Peninsula\", 1);\n      emit(\"214\", 1);\n    } else {\n      emit(\"Other Place\", 1);\n      emit(\"-1\", 1);\n    }\n  }\n}"
    }
  },
  "language": "javascript"
}

stream_doc = {
  "_id": "_design/scenario",
  "views": {
    "polarity_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.polarity>0.5 && doc.polarity<=1) {\n    emit(\"very positive\",1)\n  } else if (doc.polarity<-0.5 && doc.polarity>=-1) {\n    emit(\"very negative\",1)\n  } else if (doc.polarity > 0.1 && doc.polarity<=0.5) {\n    emit(\"positive\",1)\n  } else if (doc.polarity<-0.1 && doc.polarity>=-0.5) {\n    emit(\"negative\",1)\n  } else {\n    emit(\"netural\",1)\n  }\n}"
    },
    "subjectivity_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.subjectivity) {\n    var num = doc.subjectivity;\n    if (num <= 0.2)  {\n        emit(\"very objective\", 1);\n    } else if (num <= 0.4) {\n      emit(\"objective\", 1);\n    } else if (num <= 0.6) {\n      emit(\"normal\", 1);\n    } else if (num <= 0.8) {\n       emit(\"subjective\", 1);\n    } else if (num <= 1.0) {\n      emit(\"very subjective\", 1);\n    } else {\n      emit(\"unkown\", 1);\n    }\n  } \n}"
    },
    "language_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.lang) {\n    emit(doc.lang, 1);\n  }\n}"
    },
    "source_count": {
      "reduce": "_count",
      "map": "function (doc) {\n  if (doc.source) {\n    emit(doc.source, 1); \n  }\n}"
    }
  },
  "language": "javascript"
}

if __name__ == '__main__':
    cfg = cfg_handler.ConfigHandler()
    master_host = cfg.get_db_master_node() + ':' + cfg.get_db_port()
    auth = cfg.get_db_username() + ':' + cfg.get_db_password()
    server_link = 'http://' + auth + '@' + master_host
    req_link =server_link + '/{db}/_design/{design_doc}'
    

    # Upload Aurin design docs
    response = requests.put(
        req_link.format(db='aurin_employment_db', design_doc='scenario'),
        headers={"Content-Type": "application/json"},
        data=json.dumps(aurin_employment_doc))
    
    if response.status_code != 201:
        print('Error uploading')
    
    response = requests.put(
        req_link.format(db='aurin_house_price_db', design_doc='scenario'),
        headers={"Content-Type": "application/json"},
        data=json.dumps(aurin_house_price_doc))
    
    if response.status_code != 201:
        print('Error uploading')
    
    response = requests.put(
        req_link.format(db='aurin_income_db', design_doc='scenario'),
        headers={"Content-Type": "application/json"},
        data=json.dumps(aurin_income_doc))
    
    if response.status_code != 201:
        print('Error uploading')

    response = requests.put(
        req_link.format(db='aurin_migration_db', design_doc='scenario'),
        headers={"Content-Type": "application/json"},
        data=json.dumps(aurin_migration_doc))
    
    if response.status_code != 201:
        print('Error uploading')
    
    # Upload Twitter design docs
    response = requests.put(
        req_link.format(db=cfg.get_hp_db(), design_doc='scenario'),
        headers={"Content-Type": "application/json"},
        data=json.dumps(house_price_doc))
    
    if response.status_code != 201:
        print('Error uploading')
    
    response = requests.put(
        req_link.format(db=cfg.get_covid_db(), design_doc='scenario'),
        headers={"Content-Type": "application/json"},
        data=json.dumps(covid_doc))
    
    if response.status_code != 201:
        print('Error uploading')
    
    response = requests.put(
        req_link.format(db=cfg.get_lockdown_db(), design_doc='scenario'),
        headers={"Content-Type": "application/json"},
        data=json.dumps(covid_locadown_doc))
    
    if response.status_code != 201:
        print('Error uploading')
    
    response = requests.put(
        req_link.format(db=cfg.get_stream_db(), design_doc='scenario'),
        headers={"Content-Type": "application/json"},
        data=json.dumps(stream_doc))
    
    if response.status_code != 201:
        print('Error uploading')
    
    for each in cfg.get_twitter_dbs():
        response = requests.put(
            req_link.format(db=each, design_doc='languages'),
            headers={"Content-Type": "application/json"},
            data=json.dumps(languages_doc))
    
        if response.status_code != 201:
            print('Error uploading')

    
