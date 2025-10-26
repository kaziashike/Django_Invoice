Authentication Token

POST /token/

Request:

curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "ash",
    "password": "root"
  }'

------------------------------------------------
1. Create an Invoice

POST /invoices/create/

Headers:

Content-Type: application/json
Authorization: Bearer <your_token>

Body:
{
  "invoice_id": "INV-001",
  "name": "John Doe",
  "email": "john@example.com",
  "amount": "100.00",
  "status": "unpaid",
  "items": [
    {
      "invoice_item": "Product A",
      "item_unit_price": "25.00",
      "quantity": 2
    },
    {
      "invoice_item": "Product B",
      "item_unit_price": "50.00",
      "quantity": 1
    }
  ]
}


Example:

curl -X POST http://127.0.0.1:8000/api/invoices/create/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{
  "invoice_id": "INV-001",
  "name": "John Doe",
  "email": "john@example.com",
  "amount": "100.00",
  "status": "unpaid",
  "items": [
    {
      "invoice_item": "Product A",
      "item_unit_price": "25.00",
      "quantity": 2
    },
    {
      "invoice_item": "Product B",
      "item_unit_price": "50.00",
      "quantity": 1
    }
  ]
}'

-------------------------------------------
2. Get All Invoices

GET /invoices/

Example:

curl -X GET http://127.0.0.1:8000/api/invoices/ \
  -H "Authorization: Bearer <token>"

----------------------------------------------
3. Get Specific Invoice

GET /invoices/{invoice_id}/

Example:

curl -X GET http://127.0.0.1:8000/api/invoices/INV-001/ \
  -H "Authorization: Bearer <token>"

----------------------------------------------
4. Pay an Invoice

POST /invoices/{invoice_id}/pay/

Example:

curl -X POST http://127.0.0.1:8000/api/invoices/INV-001/pay/ \
  -H "Authorization: Bearer <your token>"

----------------------------------------------
5. Delete an Invoice

DELETE /invoices/{invoice_id}/delete/

Example:

curl -X DELETE http://127.0.0.1:8000/api/invoices/INV-001/delete/ \
  -H "Authorization: Bearer <your token>"
