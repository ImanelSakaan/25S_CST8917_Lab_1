import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )        
        

@app.route(route="SqlOutputFunction2", auth_level=func.AuthLevel.FUNCTION)
def SqlOutputFunction2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
        


# Define your output object structure
class Product:
    def __init__(self, name, quantity):
        self.Name = name
        self.Quantity = quantity

@app.function_name(name="SqlOutputFunction")
@app.route(route="add-product")  # POST /api/add-product
@app.output(name="$return",
            type="sql",
            command_text="dbo.Products",
            connection_string_setting="SqlConnectionString")
def main(req: func.HttpRequest) -> Product:
    try:
        req_body = req.get_json()
        name = req_body.get('name')
        quantity = req_body.get('quantity')

        return Product(name=name, quantity=quantity)

    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse("Invalid input", status_code=400)

        
        
        
        