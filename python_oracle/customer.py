class Customer:

    def __int__(self, customer_id,
                name,
                last_name,
                affiliation,
                customer_type,
                create_at,
                user_creation,
                modified_at,
                user_modified):
        self.customer_id = customer_id
        self.name = name
        self.last_name = last_name
        self.customer_type = customer_type
        self.create_at = create_at
        self.user_creation = user_creation
        self.modified_at = modified_at
        self.user_modified = user_modified
