require 'set'

lines = File.read(ARGV[0]).lines

sizes = {}

lines.shuffle.each do |line|
  size = line.downcase.split(', ').size
  sizes[size] ||= 0
  sizes[size] = sizes[size] + 1
end

puts sizes.inspect
