from django.views.generic import TemplateView


class Error400View(TemplateView):
    """Test view for 400 error"""

    template_name = "400.html"

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context["title"] = "Error 400"
        return context


class Error403View(TemplateView):
    """Test view for 403 error"""

    template_name = "403.html"

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context["title"] = "Error 403"
        return context


class Error404View(TemplateView):
    """Test view for 404 error"""

    template_name = "404.html"

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context["title"] = "Error 404"
        return context


class Error500View(TemplateView):
    """Test view for 500 error"""

    template_name = "500.html"

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context["title"] = "Error 500"
        return context