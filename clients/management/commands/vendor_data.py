from django.core.management.base import BaseCommand
from vendors.models import Vendor, VendorCategory


class Command(BaseCommand):
    help = 'Populate the database with the following data'

    def handle(self, *args, **options):
        if VendorCategory.objects.count() == 0:
            try:
                VendorCategory.objects.bulk_create([
                    VendorCategory(name='Web Hosting'),
                    VendorCategory(name='Domain Registrar'),
                    VendorCategory(name='SSL Certificate'),
                    VendorCategory(name='Cloud'),
                    VendorCategory(name='DNS'),
                    VendorCategory(name='CDN'),
                    VendorCategory(name='Email'),
                    VendorCategory(name='Monitoring'),
                    VendorCategory(name='Cloud'),
                    VendorCategory(name='Backup'),
                    VendorCategory(name='Database'),
                    VendorCategory(name='Payment Gateway'),
                    VendorCategory(name='SMS'),
                    VendorCategory(name='Analytics'),
                    VendorCategory(name='CRM'),
                    VendorCategory(name='Project Management'),
                    VendorCategory(name='Marketing'),
                    VendorCategory(name='Domain Registrar'),
                    VendorCategory(name='SEO'),
                    VendorCategory(name='Social Media'),
                    VendorCategory(name='Video'),
                    VendorCategory(name='Web Design'),
                    VendorCategory(name='Web Development'),
                    VendorCategory(name='Video Library'),
                    VendorCategory(name='Image Library'),
                ])
            except Exception as e:
                print(e)
        if Vendor.objects.count() == 0:
            try:
                Vendor.objects.bulk_create([
                    Vendor(name='Digital Ocean', category=VendorCategory.objects.get(name='Cloud')),
                    Vendor(name='Linode', category=VendorCategory.objects.get(name='Cloud')),
                    Vendor(name='AWS', category=VendorCategory.objects.get(name='Cloud')),
                    Vendor(name='Google Cloud', category=VendorCategory.objects.get(name='Cloud')),
                    Vendor(name='Cloudflare', category=VendorCategory.objects.get(name='CDN')),
                    Vendor(name='Cloudfront', category=VendorCategory.objects.get(name='CDN')),
                    Vendor(name='Fastly', category=VendorCategory.objects.get(name='CDN')),
                    Vendor(name='Akamai', category=VendorCategory.objects.get(name='CDN')),
                    Vendor(name='Google Domains', category=VendorCategory.objects.get(name='Domain Registrar')),
                    Vendor(name='Namecheap', category=VendorCategory.objects.get(name='Domain Registrar')),
                    Vendor(name='GoDaddy', category=VendorCategory.objects.get(name='Domain Registrar')),
                    Vendor(name='Name.com', category=VendorCategory.objects.get(name='Domain Registrar')),
                    Vendor(name='Hover', category=VendorCategory.objects.get(name='Domain Registrar')),
                    Vendor(name='Gandi', category=VendorCategory.objects.get(name='Domain Registrar')),
                    Vendor(name='Dnsimple', category=VendorCategory.objects.get(name='DNS')),
                    Vendor(name='Cloudflare', category=VendorCategory.objects.get(name='DNS')),
                    Vendor(name='Google Domains', category=VendorCategory.objects.get(name='DNS')),
                    Vendor(name='Stripe', category=VendorCategory.objects.get(name='Payment Gateway')),
                    Vendor(name='PayPal', category=VendorCategory.objects.get(name='Payment Gateway')),
                    Vendor(name='Braintree', category=VendorCategory.objects.get(name='Payment Gateway')),
                    Vendor(name='Square', category=VendorCategory.objects.get(name='Payment Gateway')),
                    Vendor(name='Google Analytics', category=VendorCategory.objects.get(name='Analytics')),
                    Vendor(name='Mixpanel', category=VendorCategory.objects.get(name='Analytics')),
                    Vendor(name='Segment', category=VendorCategory.objects.get(name='Analytics')),
                    Vendor(name='Intercom', category=VendorCategory.objects.get(name='CRM')),
                    Vendor(name='Salesforce', category=VendorCategory.objects.get(name='CRM')),
                    Vendor(name='Hubspot', category=VendorCategory.objects.get(name='CRM')),
                    Vendor(name='Trello', category=VendorCategory.objects.get(name='Project Management')),
                    Vendor(name='Asana', category=VendorCategory.objects.get(name='Project Management')),
                    Vendor(name='Jira', category=VendorCategory.objects.get(name='Project Management')),
                    Vendor(name='Mailchimp', category=VendorCategory.objects.get(name='Marketing')),
                    Vendor(name='Sendgrid', category=VendorCategory.objects.get(name='Email')),
                    Vendor(name='Mailgun', category=VendorCategory.objects.get(name='Email')),
                    Vendor(name='Mandrill', category=VendorCategory.objects.get(name='Email')),
                    Vendor(name='Sendinblue', category=VendorCategory.objects.get(name='Email')),
                    Vendor(name='Mailjet', category=VendorCategory.objects.get(name='Email')),
                    Vendor(name='Postmark', category=VendorCategory.objects.get(name='Email')),
                    Vendor(name='Amazon SES', category=VendorCategory.objects.get(name='Email')),
                    Vendor(name='Envato', category=VendorCategory.objects.get(name='Image Library')),
                    Vendor(name='Unsplash', category=VendorCategory.objects.get(name='Image Library')),
                    Vendor(name='Pexels', category=VendorCategory.objects.get(name='Image Library')),
                    Vendor(name='Pixabay', category=VendorCategory.objects.get(name='Image Library')),
                    Vendor(name='Shutterstock', category=VendorCategory.objects.get(name='Image Library')),
                    Vendor(name='Adobe Stock', category=VendorCategory.objects.get(name='Image Library')),
                    Vendor(name='Getty Images', category=VendorCategory.objects.get(name='Image Library')),
                    Vendor(name='123 RF', category=VendorCategory.objects.get(name='Image Library')),
                    Vendor(name='Vimeo', category=VendorCategory.objects.get(name='Video Library')),
                    Vendor(name='YouTube', category=VendorCategory.objects.get(name='Video Library')),
                    Vendor(name='Wistia', category=VendorCategory.objects.get(name='Video Library')),
                    Vendor(name='Vidyard', category=VendorCategory.objects.get(name='Video Library')),
                ])
            except Exception as e:
                print(e)


