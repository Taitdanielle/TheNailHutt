from django.test import TestCase    

class TestLandingViews(TestCase):

    def test_get_landing_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing/includes/image__buttons.html")
        self.assertTemplateUsed(response, "landing/includes/landing_partys.html")
        self.assertTemplateUsed(response, "landing/includes/landing_products.html")
        self.assertTemplateUsed(response, "landing/includes/landing_quote.html")
        self.assertTemplateUsed(response, "landing/includes/landing_events.html")
