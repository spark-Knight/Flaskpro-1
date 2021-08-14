from flask import Flask, jsonify


app = Flask(__name__)


classesList=["English","Science","Math","IT"]
ClassesTutor=["Prerna Bajaj","Rahul","Minakshi","Hanish","Babli","Ashwani","Mahima","Tanu"]
standardList=[1,2,3,4,5,6,7,8,9,10,11,12]
staffsNames = ["Amerender","Pooja","Rakesh","Pardeep","Tara","Sunjeeda","Aliya","Islamudeen","Ghanshyam","Bhaanu","Sunita","Shankuntla","Shabila"]
officeworks = ["Amrender","Pooja","veena di"]
juggaadunit = ["shabila","veena di","Rakesh","Pardeep","Shivkali"]
paperunit = ["Pardeep","Rakesh","veena di"]
Silaiunit = ["Shabila","shivkali","veena di"]
units = ["Silaiunit","Paperunit"]
homeStaffs = ["Tara","Sunjeeda","veena di","Aliya","Islamudeen","Ghanshyam"]
children = ["aakash","aasif","manish","veer","annu","rajkumar","shiyam","komal","lali","kittu",
"simran","alka","rani","geeta","nargis","pooja","shama","jyoti","kushi","aarti","umeresh","sid","abhi","sachin",
"vishal","vishal b","sohan","raju","dev","tushar","aashish","rahul","mahua","mannu","vijay","raju cha cha"]



classes={
    "list_of_classes":classesList,
    "number_of_classes":len(classesList),
    "list_of_tutors":ClassesTutor,
    "number_of_tutors":len(ClassesTutor),
    "standard":standardList,
}




staffs={"staffs_names" : staffsNames,
        "number_of_staffs" : len(staffsNames),
        "staffs_of juggaad_unit" : {
            "units": units,
            "unit_staff" : juggaadunit,
            "In_Silaiunit" : {
                "S_unit_staffs" : Silaiunit,
                "no._S_unit_staffs" : len(Silaiunit)
            },
            "In_Paperunit" : {
                "p_unit_staffs" : paperunit,
                "no._p_unit_staffs" : len(paperunit)
            },

        },    
            "Home_staffs" : {
                "home_Staffs" : homeStaffs,
                "no._home_staffs" : len(homeStaffs)
            }

    }


chil={"number_of_children":len(children),
      "names_of_children":"children"
      }    

# print(staffs["staffs_of juggaad_unit"])


@app.route('/')
def main():
    return "hello Karm"



@app.route('/classes')
def classess():
    return jsonify({
        "About_classes": classes,
    }) 


@app.route('/Staffs')
def staffss():
    return jsonify({
        "about_staffs": staffs
    })


@app.route('/juggaad_unit')
def unitss():
    return jsonify({
        "about_staffs": staffs["staffs_of juggaad_unit"]
    })

@app.route('/children')
def child():
    return jsonify({
         "about_children" : children
    })




if __name__ == '__main__':
    app.run()
