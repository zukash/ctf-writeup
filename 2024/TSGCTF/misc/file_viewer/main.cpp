#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <string_view>
#include <memory>
#include <algorithm>
#include <cstdlib>
#include <limits>

struct Item {
    std::string_view str;
    bool is_redacted;
};

std::unordered_map<std::string, std::string> arena;
Item items[10];

void output_content(const Item& item)
{
    bool is_printable = std::all_of(item.str.begin(), item.str.end(), [](char c) {
        return std::isprint(c) || c == '\n';
    });

    if (item.is_redacted)
    {
        std::cout << "content: **redacted**" << std::endl;
    }
    else if (!is_printable) {
        std::cout << "content: **binary**" << std::endl;
    }
    else {
        std::cout << "content: " << item.str << std::endl;
    }
}

std::unique_ptr<std::string> file_reader(const std::string& filename)
{
    if (filename.find("/proc") != std::string::npos)
    {
        std::cout << "You are a hacker :(" << std::endl;
        std::exit(0);
    }

    std::ifstream file(filename);
    if (!file)
    {
        std::cout << "Failed to open file." << std::endl;
        return nullptr;
    }

    // Check file size
    auto begin_pos = file.tellg();
    file.seekg(0, std::ios::end);
    auto size = file.tellg() - begin_pos;
    if (size > 1024 * 1024)
    {
        std::cout << "File too large." << std::endl;
        return nullptr;
    }
    file.seekg(begin_pos);

    // Read file content
    auto content = std::make_unique<std::string>(std::istreambuf_iterator<char>(file), std::istreambuf_iterator<char>());

    std::cout << "Read " << size << " bytes." << std::endl;
    return content;
}

void update_items(int index, std::unique_ptr<std::string> content, const std::string& filename)
{
    std::string_view str = *content;
    if (!items[index].str.empty())
    {
        output_content(items[index]);
        std::cout << "Overwrite loaded file? (y/n) > " << std::flush;
        char choice;
        std::cin >> choice;
        if (choice != 'y')
        {
            return;
        }
    }
    items[index].str = str;

    if (filename.find("flag") != std::string::npos)
    {
        items[index].is_redacted = true;
    }
    else
    {
        items[index].is_redacted = false;
    }
    arena[filename] = std::move(*content);
}

void load_file(int index, const std::string& filename)
{
    if (index < 0 || index >= 10)
    {
        std::cout << "Invalid index. Must be between 0 and 9." << std::endl;
        return;
    }

    if (arena.find(filename) != arena.end())
    {
        items[index].str = arena[filename];
        items[index].is_redacted = false;
        return;
    }

    auto content = file_reader(filename);
    if (!content)
        return;
    update_items(index, std::move(content), filename);
}

void read_file(int index)
{
    if (index < 0 || index >= 10 || items[index].str.empty())
    {
        std::cout << "No file loaded at this index." << std::endl;
        return;
    }

    output_content(items[index]);
}

int main()
{
    int choice;
    int index;
    std::string filename;
    while (true)
    {
        std::cout << "1. load_file\n2. read\n3. bye\nchoice > " << std::flush;
        std::cin >> choice;

        switch (choice)
        {
        case 1:
            std::cout << "index > " << std::flush;
            if (!(std::cin >> index)) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "Invalid index." << std::endl;
                continue;
            }
            std::cout << "filename > " << std::flush;
            std::cin >> filename;
            load_file(index, filename);
            break;
        case 2:
            std::cout << "index > " << std::flush;
            if (!(std::cin >> index)) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "Invalid index." << std::endl;
                continue;
            }
            read_file(index);
            break;
        default:
            std::cout << "Goodbye!" << std::endl;
            return 0;
        }
    }
}
