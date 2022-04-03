import json

# def func_body_writer(func_name,return_type,params):
#     f_rpc.write("""\tresponse = server.%s("""%func_name)
#     p_names = []
#     for param in params:
#         p_names.append(param['parameter_name'])
#     str_param = ','.join(p_names)   
#     f_rpc.write("%s)\n\treturn response\n"%str_param)
#     f_rpc.flush()

def write_imports(f_rpc,pip_imports,external_imports):
    """
    write import statements
    """
    """
    write pip imports
    pip import format:
    {
        "name": "sklearn",
        "classes": ["tree"]
    }
    """
    for pip_import in pip_imports:
        # f_rpc.write("import %s\n"%pip_import['name'])
        for cls in pip_import['classes']:
            f_rpc.write("from %s import %s\n"%(pip_import['name'],cls))
    
    # write external imports
    for external_import in external_imports:
        f_rpc.write("import %s\n"%external_import)
    
    #write flask imports
    f_rpc.write("from flask import Flask, request, jsonify\n")
    #write flask-restful imports
    f_rpc.write("from flask_restful import Resource, Api\n")
    #write interface_class import
    f_rpc.write("import ModelInterface\n")
    f_rpc.write("\n")
    f_rpc.flush()

def write_poc_class_route(f_rpc,poc_args):
    """
    write code to route poc class
    """
    f_rpc.write("""\nclass %s(Resource):\n"""%poc_args['class-name'])
    f_rpc.write("""\tdef post(self):\n""")
    f_rpc.write("""\t\trequest_data = request.get_json()\n""")
    #convert request_data to dataframe
    # f_rpc.write("""\t\tdf = DataFrame(request_data,index=[0])\n""")
    #create ModelInterface object
    f_rpc.write("""\t\tdf = request_data.get('temp', 0)\n""")
    f_rpc.write("""\t\tmodel = ModelInterface.POC_ModelInterface()\n""")
    #call poc function
    f_rpc.write("""\t\tresponse = model.poc(df)\n""")
    #return response
    # f_rpc.write("""\t\tres = {
	# 		'status_code': 200,
	# 		'response': response
	# 	}\n""")
    f_rpc.write("""\t\treturn response\n""")
    
    f_rpc.write("\n")

    f_rpc.flush()

def write_init_app(f_rpc):
    """
    write code to initiliaze app
    """
    f_rpc.write("""\napp = Flask(__name__)\napi = Api(app)\n""")
    f_rpc.flush()


def init(dir):
    """
    main drive function to write server.py
    """
    f_contract = open(dir+'/contract.json')
    content = json.load(f_contract)
    
    """
    rpc_server has:
    1. interface_object
    2. poc function call
    3. imports
    """
    f_rpc= open(dir+"/rpc_server.py","w+")
    write_imports(f_rpc,content['requirement-pip'],content['requirement-external'])
    write_init_app(f_rpc)
    write_poc_class_route(f_rpc,content["poc-args"])
    
    #attach poc to resources
    f_rpc.write("api.add_resource(Predict, '/predict')\n")
    f_rpc.write("if __name__ == '__main__':\n")
    f_rpc.write("\tapp.run(debug=True,host='0.0.0.0')\n")
    f_rpc.flush()
    f_rpc.close()
    # for func in func_list:
    #     write_rpc(func)
    # write_func_switch(func_list)
    # write_app_run()
