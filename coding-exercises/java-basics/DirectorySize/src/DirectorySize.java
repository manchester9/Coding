package com.java;

import org.apache.commons.io.FileUtils;

import java.io.File;

public class DirectorySize {

    public static void main(String[] args) {
        long size = FileUtils.sizeOfDirectory(new File("C:/Windows"));
        System.out.println("Size: " + size + " bytes");
    }

}
