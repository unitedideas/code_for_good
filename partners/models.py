import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify

from partner.util import load_choices
from partner.fields import (
    RangeIntegerField,
    PercentageField,
)

HERE = os.path.abspath(os.path.dirname(__file__))
STATES_PATH = os.path.join(HERE, 'states.txt')

STATES = load_choices(STATES_PATH, True)

# model.FileField(uploadto=proof_of_agency_status_uh)
def proof_of_agency_status_uh(instance, filename):
    return '{}/proof_of_agency_status/{}'.format(slugify(instance.name), filename)


# model.FileField(scan_990)
def scan_990_uh(instance, filename):
    return '{}/scan_990_uh/{}'.format(slugify(instance.name), filename)

"""
h2 Agency Information
         :name
         :distributor_type, collection: %w[Agency Hospital], as: :radio_buttons
         :agency_type, collection: ['501(c)3', 'Religious Organization', 'Government Organization']
         :proof_of_agency_status, as: :file
        ul
          li 501(c)3 Letter
          li Letter of Good Standing from Denominational Headquarters
          li Government Letterhead
         :agency_mission, as: :text
         :address1
         :address2
         :city
         :state, collection: states
         :zip_code

        h2 Media Information
         :website
         :facebook
         :twitter

        h2 Agency Stability
         :founded, as: :integer, input_html: { min: 1800, max: Date.current.year }
         :form_990, as: :radio_buttons
         :scan_990, as: :file
         :program_name
         :program_description
         :program_age
         :case_management, as: :radio_buttons
         :evidence_based, as: :radio_buttons
         :evidence_based_description, as: :text
         :program_client_improvement, as: :text
         :diaper_use, collection: diaper_use, as: :check_boxes
         :other_diaper_use
         :currently_provide_diapers, as: :radio_buttons
         :turn_away_child_care, as: :radio_buttons

        h3 Program Address
         :program_address1
         :program_address2
         :program_city
         :program_state, collection: states
         :program_zip_code

        h2 Organizational Capacity
         :max_serve
         :incorporate_plan, as: :text
         :responsible_staff_position, as: :radio_buttons
         :storage_space, as: :radio_buttons
         :describe_storage_space, as: :text
         :trusted_pickup, as: :radio_buttons

        h2 Population Served
         :income_requirement_desc, as: :radio_buttons
         :serve_income_circumstances, as: :radio_buttons
         :income_verification, as: :radio_buttons
         :internal_db, as: :radio_buttons
         :maac, as: :radio_buttons

        h3 Ethnic composition of those served
         :population_black, input_html: { min: 0, max: 100 }
         :population_white, input_html: { min: 0, max: 100 }
         :population_hispanic, input_html: { min: 0, max: 100 }
         :population_asian, input_html: { min: 0, max: 100 }
         :population_american_indian, input_html: { min: 0, max: 100 }
         :population_island, input_html: { min: 0, max: 100 }
         :population_multi_racial, input_html: { min: 0, max: 100 }
         :population_other, input_html: { min: 0, max: 100 }

        h3 Zips served
         :zips_served

        h3 Poverty information of those served
         :at_fpl_or_below, input_html: { min: 0, max: 100 }
         :above_1_2_times_fpl, input_html: { min: 0, max: 100 }
         :greater_2_times_fpl, input_html: { min: 0, max: 100 }
         :poverty_unknown, input_html: { min: 0, max: 100 }

        h3 Ages served
         :ages_served

        h2 Executive Director
         :executive_director_name
         :executive_director_phone
         :executive_director_email

        h2 Program Contact Person
         :program_contact_name
         :program_contact_phone
         :program_contact_mobile
         :program_contact_email

        h2 Diaper Pick Up Person
         :pick_up_method, collection: %w[volunteers staff courier]
         :pick_up_name
         :pick_up_phone
         :pick_up_email

        h2 Agency Distribution Information
         :distribution_times
         :new_client_times
         :more_docs_required

        h2 Sources of Funding
         :sources_of_funding, collection: funding_sources, as: :check_boxes
         :sources_of_diapers, collection: diaper_sources, as: :check_boxes
         :diaper_budget, collection: %w[N/A Yes No], as: :radio_buttons
         :diaper_funding_source, collection: %w[N/A Yes No], as: :radio_buttons



Collections:
    DIAPER_USE = [
   'Emergency supplies for families (off site)',
   'Homeless shelter',
   'Domestic violence shelter',
   'On-site residential program',
   'Outreach',
   'Alcohol/Drug Recovery',
   'Daycare',
   'Foster Care',
   'Other'
  ]

  FUNDING_SOURCES = [
    'Grants - Foundation',
    'Grants - State',
    'Grants - Federal',
    'Corporate Donations',
    'Individual Donations',
    'Other'
  ]

  DIAPER_SOURCES = [
    'Purchase Retail',
    'Purchase Wholesale',
    'Diaper Drives',
    'Diaper Drives conducted by others',
    'Other'
  ]
"""

# RangeIntegerField = models.IntegerField

# Common lengths
CHOICE_LENGTH = 2
ZIP_LENGTH = 100
NAME_LENGTH = 1024
MEDIUM_LENGTH = 1024
DESCRIPTION_LENGTH = 4096

# Makes it easy to specify an optional field

optional = {
    'blank': True,
    'null': True,
}

class Partner(models.Model):

    DISTRIBUTOR_AGENCY = 'AG'
    DISTRIBUTOR_HOSPITAL = 'HO'
    DISTRIBUTOR_TYPES = (
        (DISTRIBUTOR_AGENCY, 'Agency'),
        (DISTRIBUTOR_HOSPITAL, 'Hospital'),
    )

    AT_501C3 = '50'
    AT_RELIGIOUS_ORGANIZATION = 'RE'
    AT_GOVERNMENT_ORGANIZATION = 'GO'
    AGENCY_TYPES = (
        (AT_501C3, '501(c)3'),
        (AT_RELIGIOUS_ORGANIZATION, 'Religious Organization'),
        (AT_GOVERNMENT_ORGANIZATION, 'Government Organization'),
    )

    POAS_501C3_LETTER = '50'
    POAS_GOOD_STANDING = 'GS'
    POAS_GOVERNMENT_LETTERHEAD = 'GL'

    PROOF_OF_AGENCY_STATUS_TYPE = (
        (POAS_501C3_LETTER, '501(c)3 LETTER'),
        (POAS_GOOD_STANDING, 'Letter of Good Standing from Denominational Headquarters'),
        (POAS_GOVERNMENT_LETTERHEAD, 'Government Letterhead'),
    )

    DU_EMERGENCY_SUPPLIES = 'EM'
    DU_HOMELES_SHELTER = 'HO'
    DU_DOMESTIC_VIOLENCE_SHELTER = 'DO'
    DU_ONSITE = 'ON'
    DU_OUTREACH = 'OU'
    DU_ALCOHOL = 'AL'
    DU_DAYCARE = 'DA'
    DU_FOSTER_CARE = 'FO'
    DU_OTHER = 'OT'
    DIAPER_USE = (
       (DU_EMERGENCY_SUPPLIES, 'Emergency supplies for families (off site)'),
       (DU_HOMELES_SHELTER, 'Homeless shelter'),
       (DU_DOMESTIC_VIOLENCE_SHELTER, 'Domestic violence shelter'),
       (DU_ONSITE, 'On-site residential program'),
       (DU_OUTREACH, 'Outreach'),
       (DU_ALCOHOL, 'Alcohol/Drug Recovery'),
       (DU_DAYCARE, 'Daycare'),
       (DU_FOSTER_CARE, 'Foster Care'),
       (DU_OTHER, 'Other'),
    )

    PICKUP_VOLUNTEERS = 'VO'
    PICKUP_STAFF = 'ST'
    PICKUP_COURIER = 'CO'
    PICK_UP_METHODS = (
        (PICKUP_VOLUNTEERS, 'Volunteers'),
        (PICKUP_STAFF, 'Staff'),
        (PICKUP_COURIER, 'Courier'),
    )

    FS_FOUNDATION_GRANTS = 'FO'
    FS_STATE_GRANTS = 'ST'
    FS_FEDERAL_GRANTS = 'FE'
    FS_CORPORATE_DONATIONS = 'CO'
    FS_INDIVIDUAL_DONATIONS = 'IN'
    FS_OTHER = 'OT'
    FUNDING_SOURCES = (
        (FS_FOUNDATION_GRANTS, 'Grants - Foundation'),
        (FS_STATE_GRANTS, 'Grants - State'),
        (FS_FEDERAL_GRANTS, 'Grants - Federal'),
        (FS_CORPORATE_DONATIONS, 'Corporate Donations'),
        (FS_INDIVIDUAL_DONATIONS, 'Individual Donations'),
        (FS_OTHER, 'Other'),
    )

    DS_PURCHASE_RETAIL = 'PR'
    DS_PURCHASE_WHOLESALE = 'PH'
    DS_DIAPER_DRIVES = 'DD'
    DS_DIAPER_DRIVES_BY_OTHERS = 'DO'
    DS_OTHER = 'O'
    DIAPER_SOURCES = (
        (DS_PURCHASE_RETAIL, 'Purchase Retail'),
        (DS_PURCHASE_WHOLESALE, 'Purchase Wholesale'),
        (DS_DIAPER_DRIVES, 'Diaper Drives'),
        (DS_DIAPER_DRIVES_BY_OTHERS, 'Diaper Drives conducted by others'),
        (DS_OTHER, 'Other'),
    )

    user = models.ForeignKey(User, blank=False, null=False,
                             on_delete=models.CASCADE)

    # Angency Information
    name = models.CharField(max_length=2048, **optional)
    distributor_type = models.CharField(max_length=2,
                                        choices=DISTRIBUTOR_TYPES,
                                        **optional)
    agency_types = models.CharField(max_length=2,
                                    choices=AGENCY_TYPES,
                                    **optional)
    proof_of_agency_status = models.FileField(**optional)  # TODO: add file arguments
    proof_of_agency_status_type = models.CharField(max_length=CHOICE_LENGTH,
                                                   choices=PROOF_OF_AGENCY_STATUS_TYPE,
                                                   **optional)
    agency_mission = models.CharField(max_length=DESCRIPTION_LENGTH,
                                                   **optional)
    address_1 = models.CharField(max_length=MEDIUM_LENGTH,
                                                   **optional)
    address_2 = models.CharField(max_length=MEDIUM_LENGTH,
                                                   **optional)
    city = models.CharField(max_length=NAME_LENGTH,
                                                   **optional)
    state = models.CharField(max_length=2, choices=STATES,
                                                   **optional)
    zip_code = models.CharField(max_length=ZIP_LENGTH,
                                                   **optional)

    # Media Information
    website = models.URLField(**optional)
    facebook = models.CharField(max_length=NAME_LENGTH,
                                help_text="Facebook page name (DO NOT include the URL)",
                                                   **optional)
    twitter = models.CharField(max_length=NAME_LENGTH,
                               help_text="Twitter Handle",
                                                   **optional)

    # Agency Stability

    founded = RangeIntegerField(min=1800, max=2017,
                                                   **optional)
    form_990 = models.FileField(**optional)
    program_name = models.CharField(max_length=NAME_LENGTH,
                                                   **optional)
    program_description = models.CharField(max_length=DESCRIPTION_LENGTH,
                                                   **optional)
    # TODO: age (possibly omit)
    case_management = models.NullBooleanField(**optional)
    evidence_based = models.NullBooleanField(**optional)
    evidence_based_description = models.CharField(max_length=DESCRIPTION_LENGTH,
                                                   **optional)
    program_client_improvement = models.CharField(max_length=DESCRIPTION_LENGTH,
                                                   **optional)
    diaper_use = models.CharField(max_length=CHOICE_LENGTH, choices=DIAPER_USE,
                                                   **optional)
    other_diaper_use = models.CharField(max_length=DESCRIPTION_LENGTH,
                                                   **optional)
    currently_provide_diapers = models.NullBooleanField(**optional)
    turn_away_child_care = models.NullBooleanField(**optional)

    # Program Address
    program_address1 = models.CharField(max_length=MEDIUM_LENGTH,
                                                   **optional)
    program_address2 = models.CharField(max_length=MEDIUM_LENGTH,
                                                   **optional)
    program_city = models.CharField(max_length=NAME_LENGTH,
                                                   **optional)
    program_state = models.CharField(max_length=CHOICE_LENGTH,
                                     choices=STATES,
                                                   **optional)
    program_zip_code = models.CharField(max_length=ZIP_LENGTH,
                                                   **optional)

    # Organizational Capacity

    max_serve = models.IntegerField(help_text=('Maximum number of people '
                                               'this organization can serve'),
                                                   **optional)
    incorporate_plan = models.CharField(max_length=DESCRIPTION_LENGTH,
                                                   **optional)
    responsible_staff_position = models.NullBooleanField(**optional)
    storage_space = models.NullBooleanField(**optional)
    description_of_storage_space = models.CharField(max_length=DESCRIPTION_LENGTH,
                                                   **optional)
    trusted_pickup = models.NullBooleanField(**optional)

    # Population served
    incmome_requirement_description = models.NullBooleanField(**optional)
    serve_income_circumstances = models.NullBooleanField(**optional)
    income_verification = models.NullBooleanField(**optional)
    internal_diaper_bank = models.NullBooleanField(**optional)
    maac = models.NullBooleanField(**optional)

    # Ethnic composition of those served
    population_black = PercentageField(**optional)
    population_white = PercentageField(**optional)
    population_hispanic = PercentageField(**optional)
    population_asian = PercentageField(**optional)
    population_american_indian = PercentageField(**optional)
    population_island = PercentageField(**optional)
    population_multi_racial = PercentageField(**optional)
    population_other = PercentageField(**optional)

    # Zips served
    zip_codes_served = models.CharField(max_length=MEDIUM_LENGTH,
                                        **optional)

    # Poverty Information
    at_fpl_or_below = PercentageField(**optional)
    above_1_2_times_fpl = PercentageField(**optional)
    greater_2_times_fpl = PercentageField(**optional)
    poverty_unknown = PercentageField(**optional)

    # Ages served
    ages_served = models.CharField(max_length=MEDIUM_LENGTH,
                                        **optional)

    # Executive Director
    executive_director_name = models.CharField(max_length=MEDIUM_LENGTH,
                                        **optional)
    executive_director_phone = PhoneNumberField(**optional)
    executive_director_email = models.EmailField(**optional)

    # Program Contact Person
    program_contact_name = models.CharField(max_length=MEDIUM_LENGTH,
                                        **optional)
    program_contact_phone = PhoneNumberField(**optional)
    program_contact_mobile = PhoneNumberField(**optional)
    program_contact_email = models.EmailField(**optional)

    # Diaper Pickup Person
    pick_up_method = models.CharField(max_length=CHOICE_LENGTH,
                                      choices=PICK_UP_METHODS,
                                        **optional)
    pick_up_contact_name = models.CharField(max_length=MEDIUM_LENGTH,
                                        **optional)
    pick_up_contact_phone = PhoneNumberField(**optional)
    pick_up_contact_email = models.EmailField(**optional)

    # Agency Distribution Information
    distribution_times = models.CharField(max_length=MEDIUM_LENGTH,
                                        **optional)
    new_client_times = models.CharField(max_length=MEDIUM_LENGTH,
                                        **optional)
    more_docs_required = models.CharField(max_length=MEDIUM_LENGTH,
                                        **optional)

    # Sources of Funding
    funding_sources = models.CharField(max_length=CHOICE_LENGTH,
                                         choices=FUNDING_SOURCES,
                                        **optional)
    sources_of_diapers = models.CharField(max_length=CHOICE_LENGTH,
                                            choices=DIAPER_SOURCES,
                                        **optional)
    diaper_budget = models.NullBooleanField(**optional)
    diaper_funding_source = models.NullBooleanField(**optional)
