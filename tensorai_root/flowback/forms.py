from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from flowback.models import Well_Profile, Well_Data
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class CrispyModelForm(forms.ModelForm):
    class Meta:
        model = Well_Profile
        fields = '__all__'
        widgets = {
        'well_name': forms.TextInput(attrs={'placeholder': 'Please Enter Well Name', 'required': True}),
        }

    def __init__(self, *args, **kwargs):
        super(CrispyModelForm, self).__init__(*args, **kwargs)
        self.fields['initial_shut_in_psi'].label = "Initial Shut In Pressure (psi)"
        self.fields['initial_res_psi'].label = "Initial Reservoir Pressure (psi)"
        self.fields['total_frac_fluid'].label = "Total Frac Fluid Pumped (bbl)"
        self.fields['total_sand_pumped'].label = "Total Frac Sand Pumped (lb)"
        self.fields['prod_path_diameter'].label = "Diameter of flowpath (in)"
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('Submit', 'Submit'))


class CrispyDataForm(forms.ModelForm):
    class Meta:
        model = Well_Data
        fields = ('data_well_name','data_hour','data_tubing_psi','data_csg_psi','data_choke_size','data_sep_psi','data_oil_rate','data_water_rate','data_gas_rate','data_flowline_psi','data_chlorides','data_sand_percent','data_h2s','data_remarks')
        widgets = {
            #'well_name': forms.ChoiceField(choices=well_choice_gen()),
        }
    def __init__(self, *args, **kwargs):
         super(CrispyDataForm, self).__init__(*args, **kwargs)
         self.fields['data_well_name'].label = "Well name"
         #self.fields['data_date'].label = "Date (mm/dd/yyyy)"
         self.fields['data_hour'].label = "Total hours on flowback"
         self.fields['data_tubing_psi'].label = "Tubing pressure (psi)"
         self.fields['data_csg_psi'].label = "Casing pressure (psi)"
         self.fields['data_choke_size'].label = "Choke size (xx/64 or xxx/128)"
         self.fields['data_sep_psi'].label = "Separator pressure (psi)"
         self.fields['data_oil_rate'].label = "Oil rate (bbl/hr)"
         self.fields['data_water_rate'].label = "Water rate (bbl/hr)"
         self.fields['data_gas_rate'].label = "Gas rate (mcf/d)"
         self.fields['data_flowline_psi'].label = "Flowline pressure (psi)"
         self.fields['data_chlorides'].label = "Chlorides (ppm)"
         self.fields['data_sand_percent'].label = "Sand percent (%/10mL)"
         self.fields['data_h2s'].label = "H2S (ppm)"
         self.fields['data_remarks'].label = "Comments"
         # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
         self.helper = FormHelper(self)
        # You can dynamically adjust your layout
         self.helper.layout = Layout(
                 Div(
                     Div('data_well_name', css_class='span12'),
                     #Div('data_date', css_class='span12'),
                     Div('data_hour', css_class='span12'),
                     Div('data_tubing_psi', css_class='span12'),
                     Div('data_csg_psi', css_class='span12'),
                     Div('data_choke_size', css_class='span12'),
                     Div('data_sep_psi', css_class='span12'),
                     Div('data_oil_rate', css_class='span12'),
                     Div('data_water_rate', css_class='span12'),
                     Div('data_gas_rate', css_class='span12'),
                     Div('data_flowline_psi', css_class='span12'),
                     Div('data_chlorides', css_class='span12'),
                     Div('data_sand_percent', css_class='span12'),
                     Div('data_h2s', css_class='span12'),
                     Div('data_remarks', css_class='span12'),
                 css_class='row'),
     )
         self.helper.layout.append(Submit('Submit', 'Submit'))
