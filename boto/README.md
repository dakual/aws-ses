aws ses verify-email-identity --email-address daghan.altunsoy@gmail.com

aws ses send-email --from sender@domain.com --to receiver@domain.com --text "This is for those who cannot read HTML." --html "<h1>Hello World</h1><p>This is a pretty mail with HTML formatting</p>" --subject "Hello World"
