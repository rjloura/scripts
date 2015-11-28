require 'net/smtp'
msg = <<END  
From: Name <From addr>
To: Name <To addr>
Subject: Test email

This is a test... this is only a test
END


Net::SMTP.start(<smtp server>,
								25, #Port
								'localhost',
								<username>, #Username
								<password>, #Password
								:plain) do |smtp|
	smtp.send_message msg, <From addr>, <To addr>
end

