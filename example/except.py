# keyboard exception ctrl + c
database = [1,2,3,4]
for record in database:
    try:
        process(record)
        if changed:
            update(record)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        # report error and proceed
	pass

