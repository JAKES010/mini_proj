def find_record(fellow_id, resource_id):
    for record in borrow_records:
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:
            return record
    return None

def borrow(fellow_id, resource_id, qty):
    if fellow_id not in fellows:
        return "Unknown fellow"
    resource = find_resource(resource_id)
    if resource is None:
        return "Unknown resource"
    if qty <= 0:
        return "Quantity must be greater than 0"
    if qty > resource["___"]:
        return "Not enough stock"

    # all checks passed: now change data
    resource["available"] = resource["available"] - qty
    record = find_record(fellow_id, resource_id)
    if record is None:
        borrow_records.append({"fellow_id": fellow_id, "resource_id": resource_id, "count": qty})
    else:
        record["count"] = record["count"] + qty
    return "Borrowed successfully"

def find_resource(resource_id):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None

fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
borrow_records = []
