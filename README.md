# 2wenos_DeveloperHub
instead of show the coders our code on github, we are going to show the clients our templates or 1page app in action life


Final Backup
Full secure system + with error Handling

Next_step:
Focus on Login and signup errors



First Error
sqlalchemy.exc.InvalidRequestError
InvalidRequestError: One or more mappers failed to initialize - can't proceed with initialization of other mappers. Triggering mapper: 'mapped class newUrls->newurls'. Original exception was: Could not determine join condition between parent/child tables on relationship newUrls.user - there are no foreign keys linking these tables.  Ensure that referencing columns are associated with a ForeignKey or ForeignKeyConstraint, or specify a 'primaryjoin' expression.

Traceback (most recent call last)


this happend user_id = Column(Integer, ForeignKey('wrongvalue.id'))  "wrongvalue not exist" or 

#### missing ForeignKey,  user_id = Column(Integer), The noob debuger can't dedect it  
