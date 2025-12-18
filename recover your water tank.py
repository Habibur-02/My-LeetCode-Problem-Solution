
#validate this sample code with your python code.
#askld 7a873-1859a askld
# 8ac6f askld-2b02f askld
# 7c4a0-askld47975 askld
# eb64f-askld 7cfc7 askld
# 04cf1 askld-34709 askld
# b3075-askld 3c6ed askld
# askld bf8d3-ffa17 askld
# e7700-askld 47d62 askld
# 3cedd askld-4e815 askld
# 873b6 askld-95d07 askld
# aa0fd-266c5 askldaskld
# 107df-askld c5309 askld
# aa73e askld -6136c askld
# 35a81- askld 997bd askld
# fd89e askld -a7895 askld
# 5f80b-askld 6d92f askld


import random
import string
import secrets
import hashlib
import uuid
import time
from datetime import datetime
from typing import List, Optional, Dict
import argparse

class CodeGenerator:
    def __init__(self, seed: Optional[int] = None):
        """
        Initialize code generator with optional seed for reproducibility
        """
        if seed:
            random.seed(seed)
            self._use_secrets = False
        else:
            self._use_secrets = True
    
    def generate_basic_code(self, 
                           pattern: str = "XXXXX-XXXXX", 
                           charset: str = "alphanum",
                           separator: str = "-") -> str:
        """
        Generate code based on pattern with placeholders
        X = any character, L = letter, D = digit, A = alphanumeric
        """
        char_sets = {
            'letter': string.ascii_letters,
            'digit': string.digits,
            'alphanum': string.ascii_letters + string.digits,
            'hex': string.hexdigits.lower(),
            'hex_upper': string.hexdigits.upper(),
            'lower': string.ascii_lowercase,
            'upper': string.ascii_uppercase
        }
        
        charset_str = char_sets.get(charset, charset)
        
        result = []
        for char in pattern:
            if char == 'X':  # Any from charset
                result.append(self._secure_random_choice(charset_str))
            elif char == 'L':  # Letter only
                result.append(self._secure_random_choice(string.ascii_letters))
            elif char == 'D':  # Digit only
                result.append(self._secure_random_choice(string.digits))
            elif char == 'A':  # Alphanumeric
                result.append(self._secure_random_choice(string.ascii_letters + string.digits))
            elif char == 'H':  # Hex lowercase
                result.append(self._secure_random_choice(string.hexdigits.lower()))
            elif char == 'H':  # Hex uppercase
                result.append(self._secure_random_choice(string.hexdigits.upper()))
            else:
                result.append(char)
        
        return ''.join(result)
    
    def generate_uuid_based(self, 
                           version: int = 4,
                           format_type: str = "short") -> str:
        """
        Generate UUID-based codes
        """
        if version == 1:
            uid = uuid.uuid1()
        elif version == 4:
            uid = uuid.uuid4()
        else:
            uid = uuid.uuid4()
        
        uid_str = str(uid)
        
        if format_type == "short":
            # Take first 5 and last 5 chars of hex, separated by dash
            return f"{uid_str[:5]}-{uid_str[-5:]}"
        elif format_type == "numeric":
            # Convert to numeric string
            return str(int(uid.int % 1e10)).zfill(10)[:10]
        else:
            # Full UUID with dashes removed
            return uid_str.replace('-', '')
    
    def generate_timestamp_based(self,
                                format_type: str = "hex",
                                include_date: bool = True) -> str:
        """
        Generate timestamp-based codes
        """
        timestamp = time.time()
        dt = datetime.now()
        
        if format_type == "hex":
            # Convert timestamp to hex
            hex_str = hex(int(timestamp * 1000))[2:]  # Remove '0x' prefix
            
            # Take parts for formatting
            if len(hex_str) >= 10:
                part1 = hex_str[:5]
                part2 = hex_str[5:10]
                return f"{part1}-{part2}"
            else:
                padded = hex_str.ljust(10, '0')
                return f"{padded[:5]}-{padded[5:10]}"
        
        elif format_type == "alphanum":
            # Combine date and random
            if include_date:
                date_part = dt.strftime("%y%m%d")  # YYMMDD
                random_part = ''.join(self._secure_random_choice(string.ascii_letters + string.digits) 
                                    for _ in range(4))
                return f"{date_part}-{random_part}"
            else:
                return self.generate_basic_code("XXXXX-XXXXX")
    
    def generate_hashed_code(self, 
                           base_string: Optional[str] = None,
                           algorithm: str = "md5",
                           format_type: str = "dashed") -> str:
        """
        Generate codes from hash of a base string
        """
        if base_string is None:
            base_string = str(time.time()) + str(random.random())
        
        # Create hash
        if algorithm == "md5":
            hash_obj = hashlib.md5(base_string.encode())
        elif algorithm == "sha1":
            hash_obj = hashlib.sha1(base_string.encode())
        elif algorithm == "sha256":
            hash_obj = hashlib.sha256(base_string.encode())
        else:
            hash_obj = hashlib.md5(base_string.encode())
        
        hex_digest = hash_obj.hexdigest()
        
        if format_type == "dashed":
            return f"{hex_digest[:5]}-{hex_digest[5:10]}"
        elif format_type == "grouped":
            # Format like XXXXX-XXXXX-XXXXX
            parts = [hex_digest[i:i+5] for i in range(0, 15, 5)]
            return '-'.join(parts)
        else:
            return hex_digest[:10]
    
    def generate_pronounceable(self, 
                             syllables: int = 3,
                             separator: str = "-") -> str:
        """
        Generate pronounceable codes using consonant-vowel patterns
        """
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        digits = '0123456789'
        
        code_parts = []
        
        for _ in range(syllables):
            syllable = ""
            # Alternating consonant-vowel pattern
            for j in range(3):  # 3 chars per syllable
                if j % 2 == 0:  # Even positions: consonants or digits
                    if random.random() > 0.7:  # 30% chance for digit
                        syllable += self._secure_random_choice(digits)
                    else:
                        syllable += self._secure_random_choice(consonants)
                else:  # Odd positions: vowels
                    syllable += self._secure_random_choice(vowels)
            code_parts.append(syllapse)
        
        # Add a final numeric part
        numeric_part = ''.join(self._secure_random_choice(digits) for _ in range(2))
        code_parts.append(numeric_part)
        
        return separator.join(code_parts)
    
    def generate_batch(self,
                      count: int = 10,
                      code_type: str = "basic",
                      **kwargs) -> List[str]:
        """
        Generate multiple codes at once
        """
        codes = []
        for _ in range(count):
            if code_type == "basic":
                code = self.generate_basic_code(**kwargs)
            elif code_type == "uuid":
                code = self.generate_uuid_based(**kwargs)
            elif code_type == "timestamp":
                code = self.generate_timestamp_based(**kwargs)
            elif code_type == "hashed":
                code = self.generate_hashed_code(**kwargs)
            elif code_type == "pronounceable":
                code = self.generate_pronounceable(**kwargs)
            else:
                code = self.generate_basic_code(**kwargs)
            
            codes.append(code)
        
        return codes
    
    def validate_code(self, 
                     code: str, 
                     pattern: str = "XXXXX-XXXXX") -> bool:
        """
        Validate if code matches pattern
        """
        if len(code) != len(pattern):
            return False
        
        for c, p in zip(code, pattern):
            if p == 'X':  # Any alphanumeric
                if not c.isalnum():
                    return False
            elif p == 'L':  # Letter
                if not c.isalpha():
                    return False
            elif p == 'D':  # Digit
                if not c.isdigit():
                    return False
            elif p == 'A':  # Alphanumeric
                if not c.isalnum():
                    return False
            elif p == 'H':  # Hex
                if c.lower() not in '0123456789abcdef':
                    return False
            elif p not in ['X', 'L', 'D', 'A', 'H']:  # Fixed character
                if c != p:
                    return False
        
        return True
    
    def _secure_random_choice(self, sequence: str) -> str:
        """
        Use secure random if available, fallback to regular random
        """
        if self._use_secrets and len(sequence) > 0:
            return secrets.choice(sequence)
        else:
            return random.choice(sequence)
    
    def get_statistics(self, codes: List[str]) -> Dict:
        """
        Get statistics about generated codes
        """
        if not codes:
            return {}
        
        total_chars = sum(len(code) for code in codes)
        avg_length = total_chars / len(codes)
        
        # Count character types
        char_types = {
            'letters': 0,
            'digits': 0,
            'special': 0,
            'dashes': 0
        }
        
        for code in codes:
            for char in code:
                if char.isalpha():
                    char_types['letters'] += 1
                elif char.isdigit():
                    char_types['digits'] += 1
                elif char == '-':
                    char_types['dashes'] += 1
                else:
                    char_types['special'] += 1
        
        return {
            'total_codes': len(codes),
            'average_length': avg_length,
            'character_types': char_types,
            'unique_codes': len(set(codes)),
            'duplicates': len(codes) - len(set(codes))
        }


class CodeFormatter:
    @staticmethod
    def format_for_display(codes: List[str], 
                          per_line: int = 5) -> str:
        """Format codes for display"""
        lines = []
        for i in range(0, len(codes), per_line):
            line = "  ".join(codes[i:i+per_line])
            lines.append(line)
        return "\n".join(lines)
    
    @staticmethod
    def save_to_file(codes: List[str], 
                    filename: str = "generated_codes.txt"):
        """Save codes to file"""
        with open(filename, 'w') as f:
            for code in codes:
                f.write(f"{code}\n")
        print(f"Saved {len(codes)} codes to {filename}")
    
    @staticmethod
    def export_csv(codes: List[str], 
                  filename: str = "codes.csv"):
        """Export codes to CSV"""
        import csv
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Index', 'Code'])
            for i, code in enumerate(codes, 1):
                writer.writerow([i, code])
        print(f"Exported {len(codes)} codes to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Generate random string codes")
    parser.add_argument("-n", "--count", type=int, default=10, 
                       help="Number of codes to generate")
    parser.add_argument("-t", "--type", default="basic",
                       choices=["basic", "uuid", "timestamp", "hashed", "pronounceable"],
                       help="Type of code to generate")
    parser.add_argument("-p", "--pattern", default="XXXXX-XXXXX",
                       help="Pattern for basic codes (X=any, L=letter, D=digit)")
    parser.add_argument("-s", "--separator", default="-",
                       help="Separator character")
    parser.add_argument("--seed", type=int, 
                       help="Seed for reproducible generation")
    parser.add_argument("--save", action="store_true",
                       help="Save codes to file")
    parser.add_argument("--csv", action="store_true",
                       help="Export to CSV")
    parser.add_argument("--stats", action="store_true",
                       help="Show statistics")
    
    args = parser.parse_args()
    
    # Create generator
    generator = CodeGenerator(seed=args.seed)
    
    # Generate codes
    print(f"\nGenerating {args.count} {args.type} codes...")
    print("=" * 50)
    
    if args.type == "basic":
        codes = generator.generate_batch(
            count=args.count,
            code_type="basic",
            pattern=args.pattern,
            separator=args.separator
        )
    else:
        codes = generator.generate_batch(
            count=args.count,
            code_type=args.type,
            separator=args.separator
        )
    
    # Display codes
    print(CodeFormatter.format_for_display(codes))
    print("=" * 50)
    
    # Show statistics if requested
    if args.stats:
        stats = generator.get_statistics(codes)
        print("\nStatistics:")
        print(f"  Total codes: {stats['total_codes']}")
        print(f"  Unique codes: {stats['unique_codes']}")
        print(f"  Duplicates: {stats['duplicates']}")
        print(f"  Average length: {stats['average_length']:.2f}")
        print("  Character distribution:")
        for char_type, count in stats['character_types'].items():
            print(f"    {char_type}: {count}")
    
    # Save to file if requested
    if args.save:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"codes_{timestamp}.txt"
        CodeFormatter.save_to_file(codes, filename)
    
    # Export to CSV if requested
    if args.csv:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"codes_{timestamp}.csv"
        CodeFormatter.export_csv(codes, filename)
    
    print(f"\nDone! Generated {len(codes)} codes.")

sample generating code= """ 
7a873-1859a 
8ac6f-2b02f 
7c4a0-47975 
eb64f-7cfc7 
04cf1-34709 
b3075-3c6ed 
bf8d3-ffa17 
e7700-47d62 
3cedd-4e815 
873b6-95d07 
aa0fd-266c5 
107df-c5309 
aa73e-6136c 
35a81-997bd 
fd89e-a7895 
5f80b-6d92f  """

if __name__ == "__main__":
    # Example usage without command line arguments
    print("String Code Generator")
    print("=" * 50)
    
    # Create generator
    gen = CodeGenerator()
    
    # Example 1: Basic codes like "bf8d3-ffa17"
    print("\n1. Basic alphanumeric codes (pattern: XXXXX-XXXXX):")
    basic_codes = gen.generate_batch(5, "basic", pattern="XXXXX-XXXXX")
    for code in basic_codes:
        print(f"  {code}")
    
    # Example 2: UUID-based codes
    print("\n2. UUID-based short codes:")
    uuid_codes = gen.generate_batch(3, "uuid", format_type="short")
    for code in uuid_codes:
        print(f"  {code}")
    
    # Example 3: Timestamp-based codes
    print("\n3. Timestamp-based hex codes:")
    time_codes = gen.generate_batch(3, "timestamp", format_type="hex")
    for code in time_codes:
        print(f"  {code}")
    
    # Example 4: Hashed codes
    print("\n4. Hashed codes (from random base):")
    hash_codes = gen.generate_batch(3, "hashed", algorithm="md5")
    for code in hash_codes:
        print(f"  {code}")
    
    # Example 5: Pronounceable codes
    print("\n5. Pronounceable codes:")
    pronounce_codes = gen.generate_batch(3, "pronounceable", syllables=2)
    for code in pronounce_codes:
        print(f"  {code}")
    
    # Validate a code
    print("\n6. Validation example:")
    test_code = gen.generate_basic_code("LLDDD-LLDDD")
    print(f"  Generated: {test_code}")
    print(f"  Valid for pattern 'LLDDD-LLDDD': {gen.validate_code(test_code, 'LLDDD-LLDDD')}")
    
    # Run command line interface
    print("\n" + "=" * 50)
    print("For more options, run: python script.py --help")
    print("Example: python script.py -n 20 -t basic -p 'LLL-DDD-LLL' --stats")
