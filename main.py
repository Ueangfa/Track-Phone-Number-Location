import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_info(raw_number: str, default_region: str = "US") -> None:
    """
    Look up basic information about a phone number.

    This function uses the `phonenumbers` library to:
    - Validate the phone number
    - Show the region (country / area)
    - Show the carrier (if known)
    - Show possible time zone(s)
    """
    try:
        # Parse the number (default_region helps if user doesn’t include +country code)
        number = phonenumbers.parse(raw_number, default_region)

        # Validate number
        if not phonenumbers.is_valid_number(number):
            print("❌ This is not a valid phone number.")
            return

        # Region (country / area)
        region_description = geocoder.description_for_number(number, "en")

        # Carrier (network)
        carrier_name = carrier.name_for_number(number, "en")

        # Time zones (list)
        time_zones = timezone.time_zones_for_number(number)

        print("\n📱 Phone Number Info")
        print("-----------------------")
        print(f"Formatted   : {phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        print(f"Region      : {region_description or 'Unknown'}")
        print(f"Carrier     : {carrier_name or 'Unknown'}")
        print(f"Time zone(s): {', '.join(time_zones) if time_zones else 'Unknown'}")

    except phonenumbers.NumberParseException as e:
        print(f"Error parsing number: {e}")


if __name__ == "__main__":
    user_input = input("Enter phone number (e.g. +14155552671): ")
    get_phone_info(user_input.strip())
